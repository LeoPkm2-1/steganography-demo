import cv2
from cv2 import CAP_PROP_FPS
from cv2 import CAP_PROP_FRAME_COUNT

vid_capture =cv2.VideoCapture('Nature.mp4')

if (vid_capture.isOpened()==False):
    print('Error opening the video file')
else:
    # get frame rate information
    # you can replace 5 with CAP_PROP_FPS as well, they are enumeration
    fps=vid_capture.get(5)
    print('Frames per second: ',fps,' FPS')
    frame_count= vid_capture(7)
    print('Frame count: ',frame_count)
    
while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret,frame = vid_capture.read()
    if ret == True:
        # cv2.imshow('Frame',frame)
        # key = cv2.waitKey(20)
        # if key == ord('q'):
        #     break
        pass
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import types
# from PIL import Image
# import imghdr

# vidcap = cv2.VideoCapture()