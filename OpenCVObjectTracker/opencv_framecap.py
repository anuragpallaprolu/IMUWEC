import numpy as np
import cv2
#HEADMD - THE HEAD MOUNTED DISPLAY PROJECT
#FRAME CAP OPENCV SCRIPT
cap = cv2.VideoCapture(0)
i=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imwrite('frame'+str(i)+'.png',gray);
    i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
