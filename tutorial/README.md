# README

## How to Run using Docker
Prequisites:  
Have Docker installed on machine. Instructions [here](https://docs.docker.com/docker-for-mac/install/)

### Run Jupyter Notebook
0. Open Terminal

1. Pull built image from [DockerHub](https://hub.docker.com/r/rguo123/rf_cond_entropy_tutorial/) by running:  
  ```
  docker pull rguo123/rf_cond_entropy_tutorial
  ```
2. Start image with the following command
  ```
  docker run -it -p 8888:8888 rguo123/rf_cond_entropy_tutorial:latest bash
  ```
   You will ssh into running docker container.
  
3. Start notebook with the command:  
  ```
  jupyter notebook --ip 0.0.0.0 --allow-root --no-browser
  ```
4. A url that looks like the following should appear:
  ```
  Copy/paste this URL into your browser when you connect for the first time,
   to login with a token:
   http://(containerid or 127.0.0.1):8888/?token=<long token>

  ```
5. Copy URL into your browser and replace whatever is in <(containerid or 127.0.0.1)> with "localhost"
  ```
  http://localhost:8888/?token=....
  ```
   You should now be able to access the jupyter notebook.
