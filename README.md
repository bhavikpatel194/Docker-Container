# CS612-Assignment-5_Docker-Container_RESTful webiste

Requests:
_________

1. /movies
2. /movies/id


-Setup the project with the app.py and JSON file in a single folder.

-In the docker terminal, use command "touch Dockerfile" to create the Dockerfile and setup the environment of the docker file.

-Create Docker Image by running : "docker build -t flask-image:latest ."

-Check the image created using "docker images"

-Run the app image inside a container using "docker run -d -p 5000:5000 --name flask-container flask-image"

-Check running docker container by "docker ps"
