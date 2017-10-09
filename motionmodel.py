''' Motion model that can predict motion in motion in a given frame '''
import cv2

class MotionModel:
    def Predict(self, frame_url):
        print("-> Predict")

if __name__ == '__main__':
  print("CVM motion model example")
  cap = cv2.VideoCapture('Video_001.avi')
  ret, frame = cap.read()
  print(frame.shape)

  fgbg = cv2.createBackgroundSubtractorMOG2()
  # while (1):
  #     ret, frame = cap.read()
  #     fgmask = fgbg.apply(frame)
  #     cv2.imshow('frame', fgmask)
  #     k = cv2.waitKey(30) & 0xff
  #     if k == 27:
  #         break
  cap.release()
  #cv2.destroyAllWindows()


