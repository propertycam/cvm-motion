''' Runs a motion detection service client '''

from __future__ import print_function

import grpc

import model_pb2
import model_pb2_grpc


# Run the client
def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = model_pb2_grpc.ModelStub(channel)
  prediction_request = model_pb2.PredictionRequest(image_url='http://path/to/image.jpg')
  prediction_response = stub.Predict(prediction_request)
  print("Predicted concept name: " + prediction_response.concept.name)
  print("Predicted concept score: " + str(prediction_response.concept.score))


if __name__ == '__main__':
  print("CVM motion client starting ...")
  run()

