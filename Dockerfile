# Based on instructions from 
# https://github.com/grpc/grpc-docker-library/tree/master/1.0/python

FROM grpc/python:1.0-onbuild
CMD [ "python", "./your-daemon-or-script.py" ]
