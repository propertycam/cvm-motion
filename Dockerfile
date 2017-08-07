# Dockerfile to build CVM Motion Service Image

# Built from grpc python image, more info at
# https://github.com/grpc/grpc-docker-library/tree/master/1.0/python
FROM grpc/python:1.4-onbuild

# Get service definitions
RUN git clone https://github.com/propertycam/cvm-protos.git

# Compile service definitions to python source code
RUN python -m grpc_tools.protoc -Icvm-protos --python_out=. --grpc_python_out=. cvm-protos/model.proto

# Run server
#CMD [ "python", "./server.py" ]



