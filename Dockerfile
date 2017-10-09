# Dockerfile to build CVM Motion Service Image

# Based on https://hub.docker.com/r/jjanzic/docker-python3-opencv/
FROM jjanzic/docker-python3-opencv

# Create directory store app source code
RUN mkdir /app
WORKDIR /app

# Copy source code
COPY . /app

# Built from grpc python image, more info at
# https://github.com/grpc/grpc-docker-library/tree/master/1.0/python
#FROM grpc/python:1.4-onbuild

# Get service definitions
#RUN git clone https://github.com/propertycam/cvm-protos.git

# Compile service definitions to python source code
#RUN python -m grpc_tools.protoc -Icvm-protos --python_out=. --grpc_python_out=. cvm-protos/model.proto

# Run server
#CMD [ "python", "./server.py" ]



