''' Motion model that can predict motion in motion in a given frame '''
import cv2
import os

class MotionModel:
    def Predict(self, frame_url):
        print("-> Predict")

# Predict motion in frames from an example video
if __name__ == '__main__':

    print("CVM motion model example")

    # Open example vieo
    cap = cv2.VideoCapture('Video_001.avi')

    # Create output directory
    if not os.path.exists('out'):
        os.mkdir('out')

    # Create background subtractor
    fgbg = cv2.createBackgroundSubtractorMOG2()

    # Process video frames
    frame_count = 0;
    while(True):

        # Read next frame
        ret, frame = cap.read()
        if(ret):
            frame_count = frame_count + 1
        else:
            break;

        # Check if done reading
        if(frame_count > 100):
            break;

        # Apply background subtraction
        fgmask = fgbg.apply(frame)

        # Save foreground mask to file
        print('Processed frame ' + str(frame_count))
        file = 'out/' + str(frame_count) + '.jpg'
        cv2.imwrite(file, fgmask)


    # Release video capture and close file
    cap.release()


