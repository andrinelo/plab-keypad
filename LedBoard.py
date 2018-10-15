#Led Board - interface to the physical, Charlieplexed LED board.
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

def setup():
    #Set the proper mode via: GPIO.setmode(GPIO.BCM).
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
    GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # Set pin 1 - 6 to be an output pin and set initial value to low (off)
    return 0

def light_led():
    #Turn on one of the 6 LEDs by making the appropriate combination of input and output
    #declarations, and then making the appropriate HIGH /LOW settings on the output pins.
    return 0

def flash_all_leds(k):
    #Flash all 6 LEDs on and off for k seconds, where k is an argument of the method.
    return 0

def twinkle_all_leds(k):
    #Turn all LEDs on and off in sequence for k seconds, where k is an argument of the method.

    while True: # Run forever #Dette funker for pin = 1. Må la det stemme for k sek
        GPIO.output(1, GPIO.HIGH) # Turn on
        sleep(1)                  # Sleep for 1 second
        GPIO.output(1, GPIO.LOW)  # Turn off
        sleep(1)                  # Sleep for 1 second
    return 0

#in addition:
# methods for the lighting patterns associated with powering up (and down) the system.