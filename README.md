# Big-data-assingment1-
This project is a Dockerized data processing pipeline that performs data loading, preprocessing, exploratory analysis, visualization, and K-means clustering inside a Ubuntu-based container. The pipeline automates data transformation and analysis, ensuring all intermediate results are saved and extracted efficiently.



# =====================================

docker pull eepy0/bd-a1-image-v2 

dockerfile & dataset & vis.py : Hussein allam - 221000800
dpre.py & model.py & eda.py & github : Mohammed elbayoumi - 221000663
final.sh : Fares hany - 221000846
load.py & Integration of files : Ahmed Fouad - 2210001785
mohammed hesham - 22100----


#==============================================================#

to execute the project :
we made an enviroment in ubuntu in a container, we specfied the path for files and installed the libraries for python.
we  built an image using the following docker ine at first:

>>docker build -t bd-a1-image-v2 C:\bd-a1

to ensure that it worked we had to run it using the following line:

>>docker run -it 4e2579101bbc01ccef2f6bde4b1e30232aac8ff719edf71765b6e99947e3cd2et

incase the docker container went off, we ran it using the following code:

>>docker exec -it 4e2579101bbc01ccef2f6bde4b1e30232aac8ff719edf71765b6e99947e3cd2e /bin/bash

to upload the container on dockerhub we had to log in from the terminal first using:

>>docker login

then to upload the container for the first time we had to use this line:

>>docker tag bd-a1-image-v2 eepy0/bd-a1-image-v2

the tag specifys the version of the container. latest is done by default.
next was to push the container to docker hub bt using the following line:

>>docker push eepy0/bd-a1-image-v2

the image was pushed to dockerhub and was available to work, so if we want to update the image , we use the follwing line:

>>docker commit 4e2579101bbc01ccef2f6bde4b1e30232aac8ff719edf71765b6e99947e3cd2e eepy0/bd-a1-image-v2:latest

then we push:

>>docker push eepy0/bd-a1-image-v2

in order for our collegues  to work on this image as well, it was advised for them to use this docker line to pull the image to stat working:

>>docker pull eepy0/bd-a1-image-v2

bonus command used were:
>>touch
>>nano
>>ls
and that was all for the docker command lines used in this project.

to execute the project, simply type in the terminal of the container:

>> python3 load.py pokemon.csv

and the container will run the assignement

 
