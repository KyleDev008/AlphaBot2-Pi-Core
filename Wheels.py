import RPi.GPIO as GPIO
from time import sleep


class Wheels():
    
    def __init__(self, l_speed=30, r_speed=30, left_backward=12, left_forward=13, left_gnd=6, right_backward=20, right_forward=21, right_gnd=26):
        
        self.LEFT_BACKWARD = left_backward
        self.LEFT_FORWARD = left_forward
        self.LEFT_GND = left_gnd
        self.LEFT_PULSE = l_speed
        self.RIGHT_BACKWARD = right_backward
        self.RIGHT_FORWARD = right_forward
        self.RIGHT_GND = right_gnd
        self.RIGHT_PULSE = r_speed
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.LEFT_BACKWARD, GPIO.OUT)
        GPIO.setup(self.LEFT_FORWARD, GPIO.OUT)
        GPIO.setup(self.LEFT_GND, GPIO.OUT)
        GPIO.setup(self.RIGHT_BACKWARD, GPIO.OUT)
        GPIO.setup(self.RIGHT_FORWARD, GPIO.OUT)
        GPIO.setup(self.RIGHT_GND, GPIO.OUT)
        self.PWM_LEFT = GPIO.PWM(self.LEFT_GND, 500)
        self.PWM_RIGHT = GPIO.PWM(self.RIGHT_GND, 500)
        self.PWM_LEFT.start(self.LEFT_PULSE)
        self.PWM_RIGHT.start(self.RIGHT_PULSE)
        self.stop()
        
        
    def forward(self):
        
        self.PWM_LEFT.ChangeDutyCycle(self.LEFT_PULSE)
        self.PWM_RIGHT.ChangeDutyCycle(self.RIGHT_PULSE)
        GPIO.output(self.LEFT_BACKWARD, GPIO.LOW)
        GPIO.output(self.LEFT_FORWARD, GPIO.HIGH)
        GPIO.output(self.RIGHT_BACKWARD, GPIO.LOW)
        GPIO.output(self.RIGHT_FORWARD, GPIO.HIGH)
    
    def stop(self):
        
        self.PWM_LEFT.ChangeDutyCycle(0)
        self.PWM_RIGHT.ChangeDutyCycle(0)
        GPIO.output(self.LEFT_BACKWARD, GPIO.LOW)
        GPIO.output(self.LEFT_FORWARD, GPIO.LOW)
        GPIO.output(self.RIGHT_BACKWARD, GPIO.LOW)
        GPIO.output(self.RIGHT_FORWARD, GPIO.LOW)
            
    def backward(self):
        
        self.PWM_LEFT.ChangeDutyCycle(self.LEFT_PULSE)
        self.PWM_RIGHT.ChangeDutyCycle(self.RIGHT_PULSE)
        GPIO.output(self.LEFT_BACKWARD, GPIO.HIGH)
        GPIO.output(self.LEFT_FORWARD, GPIO.LOW)
        GPIO.output(self.RIGHT_BACKWARD, GPIO.HIGH)
        GPIO.output(self.RIGHT_FORWARD, GPIO.LOW)
    
    def left(self):
        
        self.PWM_LEFT.ChangeDutyCycle(self.LEFT_PULSE)
        self.PWM_RIGHT.ChangeDutyCycle(self.RIGHT_PULSE)
        GPIO.output(self.LEFT_BACKWARD, GPIO.HIGH)
        GPIO.output(self.LEFT_FORWARD, GPIO.LOW)
        GPIO.output(self.RIGHT_BACKWARD, GPIO.LOW)
        GPIO.output(self.RIGHT_FORWARD, GPIO.HIGH)
    
    def right(self):
        
        self.PWM_LEFT.ChangeDutyCycle(self.LEFT_PULSE)
        self.PWM_RIGHT.ChangeDutyCycle(self.RIGHT_PULSE)
        GPIO.output(self.LEFT_BACKWARD, GPIO.LOW)
        GPIO.output(self.LEFT_FORWARD, GPIO.HIGH)
        GPIO.output(self.RIGHT_BACKWARD, GPIO.HIGH)
        GPIO.output(self.RIGHT_FORWARD, GPIO.LOW)

    def set_left_pulse(self, pulse):
        
        self.LEFT_PULSE = pulse
        self.PWM_LEFT.ChangeDutyCycle(self.LEFT_PULSE)

    def set_right_pulse(self, pulse):
        
        self.RIGHT_PULSE = pulse
        self.PWM_RIGHT.ChangeDutyCycle(self.RIGHT_PULSE)
            
    def set_motor(self, right_pulse, left_pulse):
        
        if (right_pulse >= 0) and right_pulse <= 100:
            GPIO.output(self.LEFT_BACKWARD, GPIO.HIGH)
            GPIO.output(self.LEFT_FORWARD, GPIO.LOW)
        
        elif (right_pulse < 0) and (right_pulse >= -100):
            GPIO.output(self.LEFT_BACKWARD, GPIO.LOW)
            GPIO.output(self.LEFT_FORWARD, GPIO.HIGH)
        
        if (left_pulse >= 0) and left_pulse <= 100:
            GPIO.output(self.RIGHT_BACKWARD, GPIO.HIGH)
            GPIO.output(self.RIGHT_FORWARD, GPIO.LOW)
        
        elif (left_pulse < 0) and (left_pulse >= -100):
            GPIO.output(self.RIGHT_BACKWARD, GPIO.LOW)
            GPIO.output(self.RIGHT_FORWARD, GPIO.HIGH)

    def wheel_test(self):
        
        print("Forward!")
        self.forward()
        sleep(1)
        print("Stop!")
        self.stop()
        sleep(0.5)
        print("Backward!")
        self.backward()
        sleep(1)
        print("Stop!")
        self.stop()
        sleep(0.5)
        print("Left!")
        self.left()
        sleep(1)
        print("Stop!")
        self.stop()
        sleep(0.5)
        print("Right!")
        self.right()
        sleep(1)
        print("Stop!")
        self.stop()
