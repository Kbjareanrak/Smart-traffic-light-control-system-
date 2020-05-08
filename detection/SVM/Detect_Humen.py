import numpy as np
import cv2
 
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

#cap = cv2.VideoCapture('Pedestrians - 143.mp4')
img = cv2.imread('12295.jpg')

while(True):
   
   # ret, frame = cap.read()
    
   # frame = cv2.resize(frame, (640, 480))
    
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    boxes, weights = hog.detectMultiScale(img, winStride=(8,8) )
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(img, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    
       
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)