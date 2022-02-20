from time import sleep
from adafruit_servokit import ServoKit


# please set the following values as needed for your bot, as installation can differ.

h_center = 80 # horizontal servo center angle is 80
v_center = 130 # vertical servo center angle is 130
v_min_angle = 25 # vertical minimum angle of 25. This avoids potentially damaging the servo(s) and cabling
h_range = 500 # horizontal actuation range
v_range = 500 # vertical actuation range


class Servos():

    def __init__(self):

        print("Servos: Initializing...")
        # create the servo controller instance
        kit = ServoKit(channels=16)

        # set the servos
        self.horizontal = kit.servo[0]
        self.vertical = kit.servo[1]

        # set the default center angles
        self.center()
        sleep(0.01)
        print("Servos: Online!")

    def center(self):

        # set the servos to be centered
        self.horizontal.angle = h_center
        self.vertical.angle = v_center

    def h_center(self):

        # set the horizontal servo to be centered
        self.horizontal.angle = h_center

    def v_center(self):

        # set the vertical servo to be centered
        self.vertical.angle = v_center

    def release(self):

        # set the servos to be released
        self.horizontal.angle = None
        self.vertical.angle = None

    def set_actuation_range(self, horizontal=h_range, vertical=v_range):

        # set the range of motion
        self.horizontal.actuation_range = horizontal
        self.vertical.actuation_range = vertical

    def set_vertical_angle(self, angle):

        try:
            self.vertical.angle = angle
        except Exception as e:
            print(e)
        
    def set_horizontal_angle(self, angle):
        
        try:
            self.horizontal.angle = angle
        except Exception as e:
            print(e)

    def horizontal_sweep(self):

        for angle in range(self.horizontal.actuation_range):
            self.set_horizontal_angle(angle)
            sleep(0.01)

        for angle in range(self.horizontal.actuation_range):
            self.set_horizontal_angle(self.horizontal.actuation_range - angle)
            sleep(0.01)

        self.h_center()
        sleep(0.5)

    def vertical_sweep(self):

        for angle in range(v_min_angle, self.vertical.actuation_range, 1):
            self.set_vertical_angle(angle)
            sleep(0.01)

        for angle in range(self.vertical.actuation_range, v_min_angle, -1):
            self.set_vertical_angle(angle)
            sleep(0.01)

        self.v_center()
        sleep(0.5)
        
    def servo_test(self):
        self.horizontal_sweep()
        sleep(0.5)
        self.vertical_sweep()
        sleep(0.5)
        self.release()


if __name__ == "__main__":
    
    print(" > Testing Robot head Servos...")
    servos = Servos()
    servos.servo_test()
    print(" > Testing Complete!")

