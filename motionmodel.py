''' Motion model that can predict motion in motion in a given frame '''
import cv2
import os
import numpy as np

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
        if(frame_count > 1200):
            break;

        # Apply background subtraction
        fgmask = fgbg.apply(frame)

        # Remove speckle (small motion) with morphological opening
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=2)

        # Count non-zero foreground pixels
        fg_count = cv2.countNonZero(fgmask)

        # Combine input image and mask horizontally
        temp = np.zeros_like(frame)
        temp[:, :, 0] = fgmask
        temp[:, :, 1] = fgmask
        temp[:, :, 2] = fgmask
        combined = np.concatenate((frame, temp), axis=1)

        # Write frame number
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(combined, str(frame_count), (320,25), font, 0.7, (255,255,255))

        # Write fg pixel count
        cv2.putText(combined, str(fg_count), (320,50), font, 0.7, (255, 255, 255))

        # Save foreground mask to file
        print('Processed frame ' + str(frame_count))
        file = 'out/' + str(frame_count) + '.jpg'
        cv2.imwrite(file, combined)


    # Release video capture and close file
    cap.release()


