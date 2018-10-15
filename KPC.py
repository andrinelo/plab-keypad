#KPC - the keypad controller agent that coordinates activity between
# the other 3 classes along with veryifying and changing passwords.

def init_passcode_entry():
    #Clear the passcode-buffer and initiate a power up lighting sequence on the LED Board.
    # This should be done when the user first presses the keypad.
    return 0

def get_next_signal():
    #Return the override-signal, if it is non-blank; otherwise query the keypad for the next pressed key.
    return 0

def verify_login():
    #Check that the password just entered via the keypad matches that in the password file.
    #Store the result (Y or N) in the override-signal.
    # Also, this should call the LED Board to initiate the appropriate lighting pattern for login success or failure.
    return 0

def validate_passcode_change():
    #Check that the new password is legal. If so, write the new password in the password file.
    # A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
    # As in verify login, this should use the LED Board to signal success or failure in changing the password
    return 0

def light_one_led():
    #Using values stored in the Lid and Ldur slots, call the LED Board and request that LED
    #Lid be turned on for Ldur seconds.

    return 0

def flash_leds():
    #Call the LED Board and request the flashing of all LEDs.
    return 0

def twinkle_leds():
    #Call the LED Board and request the twinkling of all LEDs.
    return 0

def exit_action():
    #Call the LED Board to initiate the power down lighting sequence.
    return 0