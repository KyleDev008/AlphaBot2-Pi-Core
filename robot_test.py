from time import sleep

from LEDStrip import LEDStrip
from Wheels import Wheels
from Servos import Servos
from Joystick import Joystick





if __name__ == "__main__":

    print("> Testing Robot <")
    
    print(" > Testing LEDs...")
    led = LEDStrip(0.5)
    led.led_test()
    print(" > LED Testing Complete!")
    
    sleep(0.5)
    
    print(" > Testing Wheels...")
    wheels = Wheels()
    wheels.wheel_test()
    print(" > Wheels Testing Complete!")
    
    sleep(0.5)
    
    print(" > Testing Servos...")
    servos = Servos()
    servos.servo_test()
    print(" > Servos Testing Complete!")
    
    sleep(0.5)
    
    print(" > Testing Joystick...")
    joystick = Joystick()
    joystick.joystick_test()
    print(" > Joystick Testing Complete!")
    
    sleep(0.5)
    
    print("> Testing Complete!")