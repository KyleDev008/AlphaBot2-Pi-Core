# for the Wheels
from time import sleep
import board
import digitalio


class Wheels():
    
    def __init__(self):
        print("Wheels: Initializing...")

        self.left_wheel_bwd = digitalio.DigitalInOut(board.D12)
        self.left_wheel_bwd.direction = digitalio.Direction.OUTPUT
        self.left_wheel_fwd = digitalio.DigitalInOut(board.D13)
        self.left_wheel_fwd.direction = digitalio.Direction.OUTPUT
        self.left_wheel_ena = digitalio.DigitalInOut(board.D6)
        self.left_wheel_ena.direction = digitalio.Direction.OUTPUT

        self.right_wheel_bwd = digitalio.DigitalInOut(board.D20)
        self.right_wheel_bwd.direction = digitalio.Direction.OUTPUT
        self.right_wheel_fwd = digitalio.DigitalInOut(board.D21)
        self.right_wheel_fwd.direction = digitalio.Direction.OUTPUT
        self.right_wheel_enb = digitalio.DigitalInOut(board.D26)
        self.right_wheel_enb.direction = digitalio.Direction.OUTPUT

        print("Wheels: Online!")

    def forward(self):
        
        self.left_wheel_fwd.value = True
        self.left_wheel_ena.value = True
        
        self.right_wheel_fwd.value = True
        self.right_wheel_enb.value = True

    def reverse(self):
        
        self.left_wheel_bwd.value = True
        self.left_wheel_ena.value = True
        
        self.right_wheel_bwd.value = True
        self.right_wheel_enb.value = True

    def stop(self):

        self.left_wheel_fwd.value = False
        self.left_wheel_ena.value = False
        
        self.right_wheel_fwd.value = False
        self.right_wheel_enb.value = False
        
        self.left_wheel_bwd.value = False
        self.left_wheel_ena.value = False
        
        self.right_wheel_bwd.value = False
        self.right_wheel_enb.value = False

    def wheel_test(self):
        print("Going forward...")
        self.forward()
        sleep(0.2)
        print("Stopping...")
        self.stop()
        sleep(0.2)
        print("Going backward...")
        self.reverse()
        sleep(0.2)
        print("Stopping...")
        self.stop()

if __name__ == "__main__":

    wheels = Wheels()
    wheels.wheel_test()

    print("Done!")

