''' Runs a motion detection server '''

from concurrent import futures
import time

import grpc

import model_pb2
import model_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# MotionModel implements cvm model
class MotionModel(model_pb2_grpc.ModelServicer):

  def Predict(self, prediction_request, context):
    predicted_concept = model_pb2.Concept(name='motion', score=0.91)
    prediction_response = model_pb2.PredictionResponse(concept=predicted_concept)
    return prediction_response

# Start the server
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  model_pb2_grpc.add_ModelServicer_to_server(MotionModel(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  print("CVM motion server starting ...")
  serve()

