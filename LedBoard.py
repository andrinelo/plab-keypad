#Led Board - interface to the physical, Charlieplexed LED board.
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import time  # Import the sleep function from the time module



class LedBoard:
    pins = [13, 19, 26]

    pin_led_states = [
        [1, 0, - 1],
        [0, 1, - 1],
        [-1, 1, 0],
        [-1, 0, 1],
        [1, -1, 0],
        [0, -1, 1],
        [-1,-1,-1]
    ]


    def setup(self):

        #Set the proper mode via: GPIO.setmode(GPIO.BCM).
        GPIO.setmode(GPIO.BCM)  #Use physical pin numbering

    @staticmethod
    def set_pin(pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(LedBoard.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(LedBoard.pins[pin_index], GPIO.OUT)
            GPIO.output(LedBoard.pins[pin_index], pin_state)


    def light_led(self, led_number):
        for pin_index, pin_state in enumerate(LedBoard.pin_led_states[led_number]):
            LedBoard.set_pin(pin_index, pin_state)

    def flash_all_leds(self):
        print("Flashing all leds")
        #Flash all 6 LEDs on and off for k seconds, where k is an argument of the method.
        for x in range (0,6):
            self.light_led(x)

        sleep(3)  # Light for 3 seconds

        self.turnoff_leds()


    def turnoff_leds(self):
        self.light_led(6)

    def twinkle_all_leds(self):
        print("twinkling all leds")
        #Turn all LEDs on and off in sequence for k seconds, where k is an argument of the method.

        timeend = time.time() + 5 #current time + 5 sec

        while time.time() < timeend:
            for i in range (0,6):
                self.light_led(i)
                time.sleep(0.1)
                self.turnoff_leds()



    def light_duration(self, ind, duration):
        self.light_led(ind)
        time.sleep(duration)
        self.turnoff_leds()


    def power_up(self):
        print("powering up in led board")
        self.light_led(0)
        time.sleep(2)
        self.turnoff_leds()

    def power_down(self):
        print ("powering down in ledboard")
        self.light_led(1)
        self.light_led(3)
        self.light_led(5)
        time.sleep(2)
        self.turnoff_leds()


    #in addition:
# methods for the lighting patterns associated with powering up (and down) the system.