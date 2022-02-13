# for the LED strip
import board
import neopixel
from time import sleep


class LEDStrip():
    
    # custom constructor
    def __init__(self, level=0.5):
        print("LEDStrip: Initializing...")
        
        # const values for the LED strip
        self.LED_COUNT = 4 # Number of LED "pixels".
        self.LED_PIN = board.D18 # GPIO pin connected to the "pixels" (must support PWM!).
        self.ORDER = neopixel.GRB # order of the RGB input values of the LEDs, AlphaBot uses reversed red and green values, hence the GRB order instead of RGB
        
        # class members
        self.strip = neopixel.NeoPixel(self.LED_PIN, self.LED_COUNT, brightness=level, auto_write=False, pixel_order=self.ORDER) # neopixel instanciated LED strip with individual LED control.

        print("LEDStrip: Online!")
    
    # class functions
    def on(self):
        """Turn the LEDs on.
        
        The colour that each of them is currently set to will be used.
        """

        self.strip.show()
    
    def off(self):
        """Turn the LEDs off by setting their values to 0.
        """

        self.strip.fill((0, 0, 0))
        self.strip.show()

    def set_color(self, r=0, g=0, b=0, led=-1):
        """Set the colour of the strip, either the whole strip or only a single LED.

        Args:
            led (int, optional): The desired led to change the colour of. Defaults to -1.
            r (int, optional): The red value in the range 0 - 255. Defaults to 0.
            g (int, optional): The green value in the range 0 - 255. Defaults to 0.
            b (int, optional): The blue value in the range 0 - 255. Defaults to 0.
        """
        
        if led == -1:
            self.strip.fill((r, g, b))
        else:
            self.strip[led] = (r, g, b)

        self.strip.show()

    def set_brightness(self, level):
        """Sets the brightness level of the LEDs to the specified level.

        Args:
            level (float | int): level of LED brightness. Value must be between 0 and 1
        """
        
        self.strip.brightness = level
        self.strip.show()

    def get_brightness(self):
        """Returns the current brightness value as a float.

        Returns:
            float: current LED brightness level.
        """

        return self.strip.brightness

    def cycle_brightness(self, no_off=False):
        """Cycles through brightness levels from 0 to 1 incremented by 0.01 for each cycle.
        
        The cycle goes from the current brightness to 1 and then from 1 to 0.
        
        Args:
            no_off (bool, optional): Used to indicate if the brightness should not reach the 'off' state during the dimming cycle. Defaults to False.
        """

        if no_off == True:
            low = 0 # prevents the LEDs from turning off during cycle
        else:
            low = -1

        for level in range(int(self.get_brightness() * 100), 101, 1):
            self.set_brightness(level/100)
            self.on()
            sleep(0.01)

        for level in range(100, low, -1):
            self.set_brightness(level/100)
            self.on()
            sleep(0.01)

    def _wheel(self, pos):
        """Input a value 0 to 255 to get a colour value.
        The colours are a transition red - grenn - blue - back to red.
        
        Args:
            pos (int): desired colour value.
        """

        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)

        return (r, g, b)

    def rainbow_cycle(self, wait=0.1):
        """Cycles the LEDs through a rainbow using the wait variable to slow down or speed up the change.

        Args:
            wait (float, optional): time value to wait between colour switching. Defaults to 0.1
        """

        # for each LED in the strip, cycle through the full 0 - 255 RGB colour range.
        for rgb_value in range(255):
            for led in range(self.LED_COUNT):
                pixel_index = (led * 256 // self.LED_COUNT) + rgb_value
                self.strip[led] = self._wheel(pixel_index & 255) # the & 255 is used to set the value back to 0 when pixel_index reaches 256
            self.strip.show()
            sleep(wait)

    def led_test(self):
        self.set_color(255, 0, 0)
        for i in range(3):
            
            if i == 0:
                self.set_color(255, 0, 0)
            elif i == 1:
                self.set_color(0, 255, 0)
            elif i == 2:
                self.set_color(0, 0, 255)
            
            self.cycle_brightness(no_off=True)
        self.off()


# class test for making sure the bot class works as expected by running this file directly
if __name__ == '__main__':
    print(" > Testing Robot LED Strip...")
    led = LEDStrip(1)
    led.rainbow_cycle(0.01)
    led.on()
    sleep(1)
    led.set_brightness(0.1)
    sleep(1)
    led.set_brightness(1)
    sleep(1)
    led.off()
    print(" > Testing complete!")
