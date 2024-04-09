FROM python:3.10
EXPOSE 5000
WORKDIR /blog_api
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
# CMD ["flask", "run", "--host", "0.0.0.0"]

# FROM python:3.10 uses the python:3.10 image as a base.
# EXPOSE 5000 is basically documentation1. It tells the user of the Dockerfile that port 5000 is something the running container will use.
# WORKDIR /app does it so everything we do in the Docker image will happen in the image's /app directory.
# RUN pip install flask runs a command in the image. Here the command is pip install flask, which is what we need to run our app.
# COPY . . is a bit cryptic! It copies everything in the current folder (so app.py) into the image's current folder (so /app).
# CMD ["flask", "run", "--host", "0.0.0.0"] tells the image what command to run when you start a container. Here the command is flask run --host=0.0.0.0.


# docker build -t blog-api .
# docker run -d -p 5000:5000 blog-api

# docker with mapped volume to app directory
# docker run -dp 5000:5000 -w /app -v "$(pwd):/app" blog-api

# Explanation of the command:
# -dp 5000:5000 - same as before. Run in detached (background) mode and create a port mapping.
# -w /app - sets the container's present working directory where the command will run from.
# -v "$(pwd):/app" - bind mount (link) the host's present directory to the container's /app directory. Note: Docker requires absolute paths for binding mounts, so in this example we use pwd for printing the absolute path of the working directory instead of typing it manually.
# flask-smorest-api - the image to use.


# Production: 
# docker run -dp 5000:5000 -w /app -v "$(pwd):/app" teclado-site-flask sh -c "flask run --host 0.0.0.0"


# This is similar to how we've ran the Docker container with our local code as a volume (that's what -w /app -v "$(pwd):/app" does), but at the end of the command we're telling the container to run flask run --host 0.0.0.0 instead of the CMD line of the Dockerfile. That's what sh -c "flask run --host 0.0.0.0" does!

# Now you're ready to commit and push this to your repository and re-deploy to Render.com!