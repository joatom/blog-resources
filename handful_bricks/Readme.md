# A handful of bricks - from SQL to Pandas
Additional Resources to the blog article.
## Play with the examples
### Kaggle notebook
https://www.kaggle.com/joatom/a-handful-of-bricks-from-sql-to-pandas
### Docker Container
The Dockerfile is setup for private purpose to quickly get started and runs as root (ignoring security issues)! Don't use it on critical environments. Don't run notebooks in this container, that you don't trust. (For a proper Jupyter installation go to https://github.com/jupyter/docker-stacks/)
#### Requirements
- Linux (I haven't tried Windows or Mac.)
- Docker
#### Install

- clone repo
- If using Bigquery instead of SQLite include volume (*-v*) of google private access key (*.json) when running container. Specify path of access key in container in *sql2pandas_config.py*.


Build container:

    docker build . -t joatom/handful_bricks
    
Run container:
    
    docker run --name handful_bricks --rm -p 8889:8889 -p 8888:8888 -v ~/.gitconfig:/etc/gitconfig -v ~/git_repos:/home/git_repos --gpus all joatom/handful_bricks

Or run and keep container:

    docker run --name handful_bricks -it -p 8889:8889 -p 8888:8888 -v ~/.gitconfig:/etc/gitconfig -v ~/git_repos:/home/git_repos --gpus all joatom/handful_bricks

Using `-it` instead of `--rm` will keep the container and doesn't changes the jupyter token after restart (`docker start handful_bricks`).

#### Run notebook
If Jupyter token is unknown, unveil token by running:

    docker exec -it handful_bricks bash
    jupyter notebook list

Run jupyter lab in browser (e.g. http://localhost:8889). Open **handful_bricks.ipynb**. You are ready to go!


## Resources
- https://github.com/NVIDIA/nvidia-docker
- https://github.com/jupyter/docker-stacks/