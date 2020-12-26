from transformers import MarianMTModel, MarianTokenizer


def translate(blog_in, blog_out, header = []):

    # load pretrained model and tokenizer
    model_name = 'Helsinki-NLP/opus-mt-de-en'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # load german block post
    f_in = open(blog_in, "r")
    src_text = f_in.readlines()
    f_in.close()

    # preprocessing
    ## line break (\n) results to "I don't know."  We make it more specific:
    src_text = [s.replace('\n',' <<eol>>') for s in src_text]

    ## remove code block
    code = []
    inside_code_block = False
    for i, line in enumerate(src_text):
        if line.startswith('```') and not inside_code_block:
            # entering codeblock
            inside_code_block = True
            code += [line]
            src_text[i] = '<<code_block>>'
        elif inside_code_block and not line.startswith('```'):
            code += [line]
            src_text[i] = '<<code_block>>'
        elif inside_code_block and line.startswith('```'):
            # leaving code block
            code += [line]
            src_text[i] = '<<code_block>>'
            inside_code_block = False

    # translate
    translated = model.generate(**tokenizer.prepare_seq2seq_batch(src_text, return_tensors="pt"))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

    # postprocessing
    ## replace code_blog tags with code
    for i, line in enumerate(tgt_text):
        if line == '<<code_block>>':
            tgt_text[i] = code.pop(0)

    ## remove the eol (but keep empty list entries / lines)
    tgt_text = [s.replace('<<eol>>', '',) for s in tgt_text]
    ## remove space between ] ( to get the md link syntax right
    tgt_text = [s.replace('] (', '](',) for s in tgt_text]

    # add header
    tgt_text = header + tgt_text
    
    # write english blog post
    with open(blog_out, 'w') as f_out:
        for line in tgt_text:
            f_out.write("%s\n" % line)
    f_out.close()
