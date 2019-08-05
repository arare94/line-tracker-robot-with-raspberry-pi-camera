from Robot import Motor
from gpiozero import LineSensor
from time import sleep
import numpy as np
import cv2
speed = 32
#defining line sensors
left_sensor = LineSensor(21)
right_sensor = LineSensor(26)

#defining left and right motors
right_motor = Motor(17, 27, 22)
left_motor = Motor(23, 24, 25)
left_motor.set_speed(speed)
right_motor.set_speed(speed)



video_capture = cv2.VideoCapture(-1)
video_capture.set(3, 160)
video_capture.set(4, 120)

while(True):

    ret, frame = video_capture.read()

   
    crop_img = frame[60:120, 0:160]

  
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    
    blur = cv2.GaussianBlur(gray,(5,5),0)

    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

    _,contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M['m00'] != 0:
            
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        cx, cy = 0, 0

        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)

        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)

        if cx >= 120:
            left_motor.back()
            right_motor.go()
            print ("Turn Left!")

        if cx < 120 and cx > 50:
            left_motor.go()
            right_motor.go()
            print ("On Track!")

        if cx <= 50:
            left_motor.go()
            right_motor.back()
            print ("Turn Right")
        
            

    else:
        left_motor.go()
        right_motor.back()
        print ("Turn Right")
        print ("I don't see the line")

    #Display the resulting frame
    cv2.imshow('frame',crop_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
