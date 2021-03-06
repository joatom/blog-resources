FROM nvidia/cuda:10.0-base

ENV CONDA_DIR=/opt/conda

RUN apt update && apt -y upgrade && apt -y install curl python3-pip python3-dev less vim

RUN cd /tmp

RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

ENV PATH /opt/conda/bin:$PATH

RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
RUN conda --version
RUN conda clean -tipsy
RUN ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc

# create conda env
RUN conda update -n base -c defaults conda
RUN conda create -y -n handful_bricks python=3.6
ENV PATH /opt/conda/envs/handful_bricks/bin:$PATH
RUN conda init bash
SHELL ["bash", "-lc"]
RUN echo "conda activate handful_bricks" >> ~/.bashrc
RUN conda activate handful_bricks

# install jupyter
RUN conda install jupyter notebook
RUN conda install -c conda-forge jupyter_contrib_nbextensions 
RUN jupyter notebook --generate-config
RUN conda install nb_conda nb_conda_kernels --yes
RUN conda install jupyterlab
RUN conda install pip --yes
RUN conda install python-graphviz --yes
RUN conda install pandasql --yes
# need to intstall ipykernel from pip instead of conda
RUN pip install ipykernel
RUN pip install ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension

RUN pip install seaborn

EXPOSE 8889
EXPOSE 8888

ENTRYPOINT ["jupyter","lab","--ip=0.0.0.0","--port=8889","--allow-root"]

