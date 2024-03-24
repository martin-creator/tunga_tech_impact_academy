FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

# FROM python:3.10 uses the python:3.10 image as a base.
# EXPOSE 5000 is basically documentation1. It tells the user of the Dockerfile that port 5000 is something the running container will use.
# WORKDIR /app does it so everything we do in the Docker image will happen in the image's /app directory.
# RUN pip install flask runs a command in the image. Here the command is pip install flask, which is what we need to run our app.
# COPY . . is a bit cryptic! It copies everything in the current folder (so app.py) into the image's current folder (so /app).
# CMD ["flask", "run", "--host", "0.0.0.0"] tells the image what command to run when you start a container. Here the command is flask run --host=0.0.0.0.


# docker build -t blog-api .
# docker run -d -p 5000:5000 blog-api