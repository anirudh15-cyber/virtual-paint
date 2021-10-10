import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#adjusting the frame of the webcam
cap.set(3,320)                                #  setting width
cap.set(4,144)                                #  setting height
cap.set(10,130)                               #  setting brightness


 
# creating an empty function
def empty(a):
    pass

#creating window and taskbar
cv2.namedWindow("HSV")                                        # creating window named HSV
cv2.resizeWindow("HSV", 640, 240)                             # adjusting the window size
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)           # creating Trackbar named HUE Min
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)
 
 
while True:
 
    success, img = cap.read()                                  # reading the image
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)              # Converting the colour from rgb to HSV
 
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")  
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

 
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
 
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])      
    if cv2.waitKey(1) == ord('s'):
        arr=[[h_min,s_min,v_min,h_max,s_max,v_max]]
        print(arr)
        np.save("pens",arr)
        break
    cv2.imshow('Results', hStack)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()