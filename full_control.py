import cv2
#from gpiozero import LineSensor
import numpy as np
from time import sleep
#my module
from Robot import Motor

# function
def nothing(noth):
    pass
    


#speed of motors
speed = 0

#defining line sensors
#left_sensor = LineSensor(21)
#right_sensor = LineSensor(26)

#defining left and right motors
right_motor = Motor(17, 27, 22)
left_motor = Motor(23, 24, 25)

#setting up lists for sensors value
#l1 = []
#l2 = []

#opencv camera initalization
video_capture = cv2.VideoCapture(0)
#opencv camera resolution
video_capture.set(3, 80) #80
video_capture.set(4, 60) #60

#create trackbar for speed controlling
cv2.namedWindow("Speed Control")
cv2.createTrackbar("SPEED", "Speed Control", 0, 100, nothing)



while True:
    #set speed value from trackbar
    speed = cv2.getTrackbarPos("SPEED", "Speed Control")
    left_motor.set_speed(speed)
    right_motor.set_speed(speed)
    ret, frame = video_capture.read()
    crop_img = frame[60:120, 0:200]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0) #gb
    #print(blur)
    ret,thresh1 = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV) #thresh 60 255
    mask = cv2.erode(thresh1, None, iterations=2)

    mask = cv2.dilate(mask, None, iterations=2)
    _,contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        # appending values of last sensors
##        if left_sensor.value == 1:
##            l1.append("ok")
##        if right_sensor.value == 1:
##            l2.append("ok")
            
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])

            cy = int(M['m01']/M['m00'])
        else:
            cx, cy = 0, 0
##            speed = 15
##            left_motor.set_speed(speed)
##            right_motor.set_speed(speed)
##            left_motor.back()
##            right_motor.back()
##            print("Back")
        cv2.line(crop_img,(cx,0),(cx,720),(0,0,255),4)

        cv2.line(crop_img,(0,cy),(1280,cy),(0,0,255),4)
        cv2.drawContours(crop_img, contours, -1, (0,127,255), 4)
        
        if cx >= 120:
            
##            left_motor.set_speed(50)
##            right_motor.set_speed(50)
            left_motor.go()
            right_motor.back()
            print ("Right")

            

 

        if cx < 120 and cx > 60:
            left_motor.go()
            right_motor.go()
            print ("Go!")
            
            
            

        if cx <= 60:
##            left_motor.set_speed(50)
##            right_motor.set_speed(50)
            left_motor.back()
            right_motor.go()
            print ("Left!")
            

    else:
        pass
##        speed = 15
##        left_motor.set_speed(speed)
##        right_motor.set_speed(speed)
##        left_motor.back()
##        right_motor.back()
        
        
        #print ("Go Back There Is No Line")

 

 


    cv2.imshow('frame',crop_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        speed = 0
        del(right_motor)
        break
cv2.destroyAllWindows()
