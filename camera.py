import cv2

while True:
    cam = cv2.VideoCapture(0)
    s, im = cam.read() # captures image
    cv2.imshow("Test Picture", im) 
