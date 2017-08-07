''' Runs a motion detection service client '''

from __future__ import print_function

import grpc

import model_pb2
import model_pb2_grpc


# Run the client
def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = model_pb2_grpc.ModelStub(channel)
  predict_input = model_pb2.PredictInput(image_url='http://path/to/image.jpg')
  predict_output = stub.Predict(predict_input)
  print("Predicted concept name: " + predict_output.concept.name)
  print("Predicted concept score: " + str(predict_output.concept.score))


if __name__ == '__main__':
  print("CVM motion client starting ...")
  run()

