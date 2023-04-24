# Understanding Docker
## Prerequisites:

-   A Linux or macOS machine with administrative privileges
-   A basic understanding of the command line interface

## Objectives:

-   Understand the basics of Docker and containerization
-   Install Docker on your local machine
-   Use Docker to run and manage containers
-   Understand and create Dockerfiles to define container images
-   Use Docker Compose to manage multiple containers

## Steps:

1.  Start by installing Docker on your local machine. Refer to the official Docker documentation for instructions on installing Docker on your specific platform.
    
2.  Once Docker is installed, verify that it is running correctly by running the following command:
  
    `docker version` 
    
    This should display information about the Docker version and build.
    
3.  Use the following command to search the Docker Hub repository for a public image:

    `docker search <image name>` 
    
    Replace `<image name>` with the name of an image you are interested in, such as "nginx" or "postgres". This will display a list of public images available on Docker Hub.
    
4.  Use the following command to download and run an image:

    `docker run <image name>` 
    
    Replace `<image name>` with the name of an image you want to run. This will download the image from Docker Hub and start a container based on that image.
    
5.  Use the following command to list all running containers:
  
    `docker ps` 
    
    This will display information about all running containers, including their ID, image name, and status.
    
6.  Use the following command to stop a running container:

    `docker stop <container ID>` 
    
    Replace `<container ID>` with the ID of a running container that you want to stop. This will gracefully stop the container and exit it.
    
7.  Use the following command to remove a stopped container:

    `docker rm <container ID>` 
    
    Replace `<container ID>` with the ID of a stopped container that you want to remove. This will permanently remove the container from the system.
    
8.  Create a Dockerfile to define a custom container image. For example, you can create a simple Python application that prints "Hello, Docker!" to the console:

    `FROM python:3.9-slim-buster
    
    WORKDIR /app
    
    COPY requirements.txt .
    
    RUN pip install --no-cache-dir -r requirements.txt
    
    COPY . .
    
    CMD [ "python", "./app.py" ]` 
    
    This Dockerfile starts with the official Python 3.9 slim image, sets the working directory to `/app`, copies the `requirements.txt` file to the working directory, installs the Python dependencies, copies the rest of the files in the current directory to the working directory, and specifies the command to run the `app.py` file.
    
9.  Use the following command to build a Docker image from the Dockerfile:

    `docker build -t <image name> .` 
    
    Replace `<image name>` with a name for your custom image. This will create a new image based on the instructions in the Dockerfile.
    
10.  Use the following command to run a container based on your custom image:

`docker run -p 5000:5000 <image name>` 

Replace `<image name>` with a name for your custom image. This will start a container based on your custom image and map port 5000 on the host to port 5000 in the container.

11.  Use the following command to list all running containers:

`docker ps` 

This will display information about all running containers, including the container ID and the mapped ports.

12.  Open a web browser and navigate to `http://localhost:5000`. You should see the message "Hello, Docker!" displayed in the browser.
    
13.  Use the following command to stop and remove the container:
    
`docker stop <container ID>
docker rm <container ID>` 

Replace `<container ID>` with the ID of the container you want to stop and remove.

14.  Finally, use Docker Compose to manage multiple containers. Create a new file called `docker-compose.yml` with the following contents:

`version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"` 

This file defines a single service called `web` that builds an image from the current directory (`.`) and maps port 5000 on the host to port 5000 in the container.

15.  Use the following command to start the service defined in the `docker-compose.yml` file:

`docker-compose up` 

This will start the container defined in the `docker-compose.yml` file and display the logs in the terminal.

16.  Open a web browser and navigate to `http://localhost:5000`. You should see the message "Hello, Docker!" displayed in the browser.
    
17.  Use the following command to stop and remove the containers defined in the `docker-compose.yml` file:

`docker-compose down` 

This will gracefully stop and remove the containers.

# Docker networks
To manage Docker networks, you can use the `docker network` command. This command allows you to create, inspect, and delete networks, as well as connect and disconnect containers from them.

Some common `docker network` commands include:

-   `docker network create`: Creates a new network with the specified name and driver.
    
-   `docker network ls`: Lists all available networks on the host.
    
-   `docker network inspect`: Shows detailed information about a specific network.
    
-   `docker network connect`: Connects a container to a network.
    
-   `docker network disconnect`: Disconnects a container from a network.
    
-   `docker network rm`: Deletes a network.