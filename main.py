from Robot import Motor
from gpiozero import LineSensor
from time import sleep
import cv2




def nothing(noth):
    pass

#defining line sensors
left_sensor = LineSensor(21)
right_sensor = LineSensor(6)
status_sensor = LineSensor(5)


#cv2.namedWindow("Speed Control")
#cv2.createTrackbar("SPEED", "Speed Control", 0, 100, nothing)

speed = 30
#defining left and right motors
right_motor = Motor(17, 27, 22)
left_motor = Motor(23, 24, 25)
left_motor.set_speed(speed)
right_motor.set_speed(speed)


#main program logic loop

while True:
    #speed = cv2.getTrackbarPos("SPEED", "Speed Control")
    #left_motor.set_speed(speed)
    #right_motor.set_speed(speed)
##    print("Left sensor value is", left_sensor.value)
##    print("right sensor value is", right_sensor.value)
##    print("STATUS sensor value is", status_sensor.value)
##    sleep(1)
    try:
        if left_sensor.value < 1 and right_sensor.value < 1:
            left_motor.go()
            right_motor.go()

        if left_sensor.value > 0 and right_sensor.value > 0:
            left_motor.go()
            right_motor.go()

        if left_sensor.value < 1 and right_sensor.value > 0:
          
            left_motor.go()
            right_motor.back()

        if left_sensor.value > 0 and right_sensor.value < 1:
     
            left_motor.back()
            right_motor.go()

    except KeyboardInterrupt:
        del(left_motor)
        del(right_motor)
        

