# Dockerfile to build CVM Motion Service Image

# Built from grpc python image, more info at
# https://github.com/grpc/grpc-docker-library/tree/master/1.0/python
FROM grpc/python:1.0-onbuild

# Compile proto files to python source code


# Run server
CMD [ "python", "./server.py" ]



