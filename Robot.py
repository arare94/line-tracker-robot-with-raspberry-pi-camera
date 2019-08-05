import RPi.GPIO as io
from time import sleep
"""
2.3.4 - Arm
14.15.18 - Motor
"""

class Motor:
    io.setmode(io.BCM)
    io.setwarnings(False)
    def __init__(self, enb, in1, in2):
        self.enb = enb
        self.in1 = in1
        self.in2 = in2
        io.setup(self.in1, io.OUT)
        io.setup(self.in2, io.OUT)
        io.setup(self.enb, io.OUT)
        self.p = io.PWM(self.enb, 1000)
        

    def set_speed(self, speed):
        self.p.start(speed)

    def go(self):
        io.output(self.in1, io.HIGH)
        io.output(self.in2, io.LOW)

    def back(self):
        io.output(self.in1, io.LOW)
        io.output(self.in2, io.HIGH)

    def stop(self):
        io.output(self.in1, io.LOW)
        io.output(self.in2, io.LOW)

class Arm:
    io.setmode(io.BCM)
    io.setwarnings(False)
    def __init__(self, enb, in1, in2):
        self.enb = enb
        self.in1 = in1
        self.in2 = in2
        io.setup(self.in1, io.OUT)
        io.setup(self.in2, io.OUT)
        io.setup(self.enb, io.OUT)
        self.p = io.PWM(self.enb, 1000)

    def open(self):
        io.output(self.in1, io.HIGH)
        io.output(self.in2, io.LOW)

    def close(self):
        io.output(self.in1, io.LOW)
        io.output(self.in2, io.HIGH)

    def speed(self, speed):
        self.p.start(speed)

    def stop(self):
        io.output(self.in1, io.LOW)
        io.output(self.in2, io.LOW)
                 
        
