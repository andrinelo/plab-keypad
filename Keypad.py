#Keypad - interface to the physical keypad

def setup():
    #Set the proper mode via:
    # GPIO.setmode(GPIO.BCM).
    # Also, use GPIO functions to set the row pins
    # as outputs and the column pins as inputs.

    return 0

def do_polling():
    #Use nested loops (discussed above) to determine
    # the key currently being pressed on the keypad.

    return 0

def get_next_signal():
    #This is the main interface between the agent and the keypad.
    #It should initiate repeated calls to do polling until a key press is detected.
    return 0

