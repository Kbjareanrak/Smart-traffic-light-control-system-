from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

import socket
import sys  

host = '192.168.4.1'
port = 88  # web

print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address') 
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

# Send data to remote server
print('# Sending data to server')

# construct the argument parse and parse the arguments

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


image = cv2.imread("piccap/55/1.jpg")
image = imutils.resize(image, width=min(400, image.shape[1]))
orig = image.copy()

(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),padding=(8, 8), scale=1.05)

for (x, y, w, h) in rects:
    cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
for (xA, yA, xB, yB) in pick:
    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

A = int(len(pick))
print(A)

if(A != 0):
    if(A == 1):
        print('A = 1')
        ee = '1'
    else:
        print('A != 1')
else:
    print('No human')
    ee = '0'

request = ee.encode()
try:
    s.sendall(request)
except socket.error:
    print('Send failed')
    sys.exit()

# Receive data
print('# Receive data from server')
reply = s.recv(4096)

print (reply)

cv2.imshow("Before NMS", orig)
cv2.imshow("After NMS", image)    
cv2.waitKey(0)