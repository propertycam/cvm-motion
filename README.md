# cvm-motion
Motion detection service

CVM Motion detection service runs in Docker containers.  Install Docker
on your system to build or run the service.

## How to build Docker image

    docker build -t cvm-motion .

## How to run image in a container

Run this service's server with

    sudo docker run cvm-motion python ./server.py

Run in an ineteractive terminal

    sudo docker run -it --rm cvm-motion bash

## How to remove images


