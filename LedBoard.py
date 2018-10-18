#Led Board - interface to the physical, Charlieplexed LED board.
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

class LedBoard:


    def setup(self):
        #Set the proper mode via: GPIO.setmode(GPIO.BCM).
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
        # Set pin 1 - 6 to be an output pin and set initial value to low (off)


    def light_led(self):
        #TODO
        #Turn on one of the 6 LEDs by making the appropriate combination of input and output
        #declarations, and then making the appropriate HIGH /LOW settings on the output pins.
        pass

    def flash_all_leds(k):
        #Flash all 6 LEDs on and off for k seconds, where k is an argument of the method.
        GPIO.output(1, GPIO.HIGH)  # Turn on led 1
        GPIO.output(2, GPIO.HIGH)  # Turn on led 2
        GPIO.output(3, GPIO.HIGH)  # Turn on led 3
        GPIO.output(4, GPIO.HIGH)  # Turn on led 4
        GPIO.output(5, GPIO.HIGH)  # Turn on led 5
        GPIO.output(6, GPIO.HIGH)  # Turn on led 6

        sleep(k)  # Sleep for 1 second

        GPIO.output(1, GPIO.LOW) # turn off led 1
        GPIO.output(2, GPIO.LOW)  # turn off led 2
        GPIO.output(3, GPIO.LOW)  # turn off led 3
        GPIO.output(4, GPIO.LOW)  # turn off led 4
        GPIO.output(5, GPIO.LOW)  # turn off led 5
        GPIO.output(6, GPIO.LOW)  # turn off led 6

        print("flash all leds for k seconds complete")

    def twinkle_all_leds(k):
        #Turn all LEDs on and off in sequence for k seconds, where k is an argument of the method.

        '''
                #proposed implementation of twinkle led lights?

                time = (k/6)
                GPIO.output(1, GPIO.HIGH)  # Turn on led 1
                sleep(time)  # light for k/6 seconds
                GPIO.output(1, GPIO.LOW)  # Turn off led 1

                GPIO.output(2, GPIO.HIGH)  # Turn on led 2
                sleep(time)  # light for k/6 seconds
                GPIO.output(2, GPIO.LOW)  # Turn off led 2

                GPIO.output(3, GPIO.HIGH)  # Turn on led 3
                sleep(time)  # light for k/6 seconds
                GPIO.output(3, GPIO.LOW)  # Turn off led 3

                GPIO.output(4, GPIO.HIGH)  # Turn on led 4
                sleep(time)  # light for k/6 seconds
                GPIO.output(4, GPIO.LOW)  # Turn off led 4

                GPIO.output(5, GPIO.HIGH)  # Turn on led 5
                sleep(time)  # light for k/6 seconds
                GPIO.output(5, GPIO.LOW)  # Turn off led 5

                GPIO.output(6, GPIO.HIGH)  # Turn on led 6
                sleep(time)  # light for k/6 seconds
                GPIO.output(6, GPIO.LOW)  # Turn off led 6

                '''


        while True: # Run forever #Dette funker for pin = 1. Må la det stemme for k sek
            GPIO.output(1, GPIO.HIGH) # Turn on
            sleep(1)                  # Sleep for 1 second
            GPIO.output(1, GPIO.LOW)  # Turn off
            sleep(1)                  # Sleep for 1 second
        pass




    def power_up(self):
        #method for lighting pattern when powering up
        pass

    def power_down(self):
        #power down lights
        pass
    #in addition:
# methods for the lighting patterns associated with powering up (and down) the system.