# for the Joystick
from time import sleep
import board
import digitalio
from wheel_test import *
import RPi.GPIO as GPIO

# all joystick values are by default True, and become False when engaged

class Joystick(object):

    def __init__(self,ctr=7,a=8,b=9,c=10,d=11,buz=4):
        self.CTR = ctr
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.BUZ = buz

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.CTR,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.A,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.B,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.C,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.D,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.BUZ,GPIO.OUT)

    def beep_on(self):
        GPIO.output(self.BUZ,GPIO.HIGH)
    def beep_off(self):
        GPIO.output(self.BUZ,GPIO.LOW)

    def show_values(self):

        print(f"CTR > {GPIO.input(self.CTR)}")
        print(f"A > {GPIO.input(self.A)}")
        print(f"B > {GPIO.input(self.B)}")
        print(f"C > {GPIO.input(self.C)}")
        print(f"D > {GPIO.input(self.D)}")

    def joystick_test(self):
        print("Values Before:")
        self.show_values()
        print("Values After:")
        sleep(2)
        self.show_values()


if __name__ == "__main__":
    
    print("Values Before:")
    joystick = Joystick()
    wheels = Wheels()
    
    try:
        while True:
            
            if joystick.btn_a.value == False:
                wheels.forward()
                print("forward")
                while joystick.btn_a.value == False:
                    sleep(0.01)
            elif joystick.btn_b.value == False:
                wheels.right()
                print("right")
                while joystick.btn_b.value == False:
                    sleep(0.01)
            elif joystick.btn_c.value == False:
                wheels.left()
                print("left")
                while joystick.btn_c.value == False:
                    sleep(0.01)
            elif joystick.btn_d.value == False:
                wheels.backward()
                print("backward")
                while joystick.btn_d.value == False:
                    sleep(0.01)
            elif joystick.btn_center.value == False:
                wheels.stop()
                print("stop")
                while joystick.btn_center.value == False:
                    sleep(0.01)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
