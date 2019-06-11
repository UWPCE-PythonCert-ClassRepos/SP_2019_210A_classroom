# Docker and Docker Compose For Iterative Development
### Joe Nunnelley

## __What is Docker?__

- Docker is a containerization technology used to encapsulate services and make deployment and management of those services in production environmments easier.

- https://www.docker.com/

    #### --What Docker Can Do For Your Business / You --
    The Docker Enterprise container platform delivers immediate value to your business by reducing the infrastructure and maintenance costs of supporting your existing application portfolio while accelerating your time to market for new solutions.

    #### Dockerfile ####
    - the primary configuration definition of a docker container
    - https://docs.docker.com/engine/reference/builder/
    - example :

        ```
       FROM python:3
       ENV PYTHONUNBUFFERED 1
       RUN mkdir /code
       WORKDIR /code
       COPY requirements.txt /code/
       RUN pip install -r requirements.txt
       COPY . /code
       CMD ["python", "manage.py"]

## __What is DockerCompose?__

- DockerCompose is a way to run multiple containers as a group to simulate multi-host software systems. This allows developers to create a system on a box that can have one or more containers running and talking with one another

    - https://docs.docker.com/compose/
    - the primary configuration file for docker-compose is the docker-compse.yml.
    - example:

    ```
    version: '3'

    services:
        db:
            image: postgres
        web:
            build: .
            command: python manage.py runserver 0.0.0.0:8000
            volumes:
            - .:/code
        ports:
            - "8000:8000"
        depends_on:
            - db
        redis:
            image: "redis:alpine"



## __Using it for Development__
- Demonstrate configuring and running a group project.
- The above docker-compose file will start the following:
    - a postgres database
    - a django web server running a simple web page


### Additional Resources

- https://takacsmark.com/docker-compose-tutorial-beginners-by-example-basics/
