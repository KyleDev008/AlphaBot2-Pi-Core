# for the Joystick
from time import sleep
import board
import digitalio

# all joystick values are by default True, and become False when engaged

class Joystick():

    def __init__(self):
        print("Joystick: Initializing...")

        self.btn_center = digitalio.DigitalInOut(board.D7)
        self.btn_center.direction = digitalio.Direction.INPUT
        self.btn_a = digitalio.DigitalInOut(board.D8)
        self.btn_a.direction = digitalio.Direction.INPUT
        self.btn_b = digitalio.DigitalInOut(board.D9)
        self.btn_b.direction = digitalio.Direction.INPUT
        self.btn_c = digitalio.DigitalInOut(board.D10)
        self.btn_c.direction = digitalio.Direction.INPUT
        self.btn_d = digitalio.DigitalInOut(board.D11)
        self.btn_d.direction = digitalio.Direction.INPUT

        print("Joystick: Online!")

    def show_values(self):

        print(f"CTR > {self.btn_center.value}")
        print(f"A > {self.btn_a.value}")
        print(f"B > {self.btn_b.value}")
        print(f"C > {self.btn_c.value}")
        print(f"D > {self.btn_d.value}")

    def joystick_test(self):
        print("Values Before:")
        self.show_values()
        print("Values After:")
        sleep(2)
        self.show_values()


if __name__ == "__main__":
    
    print("Values Before:")
    joystick = Joystick()
    joystick.show_values()
    print("Values After:")
    sleep(2)
    joystick.show_values()
