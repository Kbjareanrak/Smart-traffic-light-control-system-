# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
 
img = cv2.imread('12.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


image = imutils.resize(img, width=min(400, img.shape[1]))
orig = image.copy()
 
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.03)
 
# draw the original bounding boxes
for (x, y, w, h) in rects:
	cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
 
	# draw the final bounding boxes
for (xA, yA, xB, yB) in pick:
	cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
 
# show the output images
cv2.imshow("Before NMS", orig)
cv2.imshow("After NMS", image)
cv2.waitKey(0)