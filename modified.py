import cv2
import numpy as np
load_from_disk = True
if load_from_disk:
    mycolor = np.load('pens.npy')

camera=cv2.VideoCapture(0)
#camera.set(3,640)                                                   # setting width
#camera.set(4,480)                                                   # setting height 
            
# HSV values of the colour 
#mycolor= [[55,41,136,84,255,255],                   #green colour  [hue_min, sat_min, value_min, hue_max, sat_max, value_max]
 #         [100,136,117,122,247,255],                #blue colour
  #         [12,153,155,29,255,255],                  #yellow colour
   #        [0, 134, 160, 9, 255, 255]]               #red color
        
 # BGR values of the colour
colorValue= [[0,255,0],                        # green colour      [blue, green, red]
             [255,0,0],                        # blue colour
             [0,255,255],                      #yellow colour
               [0,0,255]]                     # red colour      


myPoints =  []                               # [x , y , colorId ]

# a function to detect the contour
def findColor(img,mycolor,colorValue):                                          
    HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in mycolor:                                            # To use multiple colours in webcam
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(HSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,colorValue[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

# Function to get the tip coordinate
def getContours(img):                                                 
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)                                  #calculating the area of the contour
        if area>300:
            peri = cv2.arcLength(cnt,True)                           # calculating perimeter 
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)            #finding the corners 
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y                                          #return the coordinates of tip's center
# Function to draw on the screen
def drawScreen(myPoints,colorValue):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),15,colorValue[point[2]],cv2.FILLED)


while True:
    suc,img=camera.read()
    img = cv2.flip(img,1)                                               #flip the image horizontally
    imgResult=img.copy()
    newPoints=findColor(img,mycolor,colorValue)
    if len(newPoints)!=0:                    
        for point in newPoints:
            myPoints.append(point)
    if len(myPoints)!=0:
        drawScreen(myPoints,colorValue)
        
    cv2.imshow("Paint",imgResult)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
camera.release()
cv2.destroyAllWindows()



