import numpy as np
import cv2
 
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))


 
if cap.isOpened() == False:
    print('Unable to open the camera')
else:
    print('Start grabbing, press a key on Live window to terminate')
    cv2.namedWindow('Live');
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    while( cap.isOpened() ):
        ret,frame = cap.read()
        if ret==False:
            print('Unable to grab from the camera')
            break
         
        cv2.imshow('Live',frame)
        out.write(frame)
        #cv2.waitKey(0);
        key = cv2.waitKey(5)
        if key==255: key=-1 #Solve bug in 3.2.0
        if key >= 0:
            break
    print('Closing the camera')
 
cap.release()
cv2.destroyAllWindows()
print('bye bye!')
quit()
