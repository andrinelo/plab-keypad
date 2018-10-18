#KPC - the keypad controller agent that coordinates activity between
# the other 3 classes along with veryifying and changing passwords.
from FSM import FSM
from Keypad import Keypad
from FSMRule import FSMRule

p1 = 1
p2 = 2
p3 = 3
p4 = 4
p5 = 5
p6 = 6

class KPC:


    def __init__(self):
        self.keypad = Keypad()
        self.fsm = FSM(self)
        self.override_signal = None
        self.init_passcode_entry()


    def init_rules(self):
        self.fsm.add_rule("S-INIT", "S-READ", self.fsm.activate_is_true, self.light_led_1)

        self.fsm.add_rule("S-READ", "S-ACTIVE", self.fsm.validate_entire, self.read_to_active)
        self.fsm.add_rule("S-READ", "S-READ", self.fsm.validate_cump, self.add_to_cump)
        self.fsm.add_rule("S-READ", "S-READ", self.fsm.unvalidate_cump, self.read_wrong_nr)
        self.fsm.add_rule("S-READ", "S-INIT", "#", self.power_down)

        self.fsm.add_rule("S-ACTIVE", "S-INIT", "#", self.power_down)
        self.fsm.add_rule("S-ACTIVE", "S-ACTIVE", "1", self.light_led_1)
        self.fsm.add_rule("S-ACTIVE", "S-ACTIVE", "2", self.light_led_2)
        self.fsm.add_rule("S-ACTIVE", "S-ACTIVE", "3", self.light_led_3)
        self.fsm.add_rule("S-ACTIVE", "S-ACTIVE", "4", self.light_led_4)
        self.fsm.add_rule("S-ACTIVE", "S-ACTIVE", "5", self.light_led_5)
        self.fsm.add_rule("S-ACTIVE", "S-ACTIVE", "6", self.light_led_6)
        self.fsm.add_rule("S-ACTIVE", "S-PR1", "*", self.flash_change_state)

        self.fsm.add_rule("S-PR1", "S-PR1", FSMRule.signal_is_digit, self.add_to_dp)
        #kommentar under gjelder linje 41
        # noe feil med signal_is_digit, bare prøv å kjøre den som signal og riktig state, og se på feilmeldingen om
        #at: expected string but function found
        self.fsm.add_rule("S-PR1", "S-ACTIVE", "#", self.reset_dp)
        self.fsm.add_rule("S-PR1", "S-PR2", "*", self.flash_change_state)

        self.fsm.add_rule("S-PR2", "S-ACTIVE", "#", self.reset_dp_cump)
        self.fsm.add_rule("S-PR2", "S-PRVERIFY", self.fsm.validate_entire_pr, self.flash_change_state)
        self.fsm.add_rule("S-PR2", "S-PR2", self.fsm.validate_cump_pr, self.add_to_cump)
        #gjelder linje 50; får ikke testet uten GPIO som ikke går uten RPi
        self.fsm.add_rule("S-PR2", "S-ACTIVE", self.fsm.unvalidate_cump_pr, self.pr2_to_active)

        self.fsm.add_rule("S-PRVERIFY", "S-ACTIVE", "*",  self.verify_to_active)

        self.fsm.add_rule("S-ACTIVE", "S-INIT", "#", self.power_down)

    def init_passcode_entry(self):
        #Clear the passcode-buffer and initiate a power up lighting sequence on the LED Board.
        # This should be done when the user first presses the keypad.
        #self.light_led_1()
        #kommenterte ut denne fordi den ble forvirrende under testingen
        pass

    def get_next_signal(self):
        if self.override_signal:
            return self.override_signal
        else:
            return self.keypad.get_next_signal()

        #Return the override-signal, if it is non-blank; otherwise query the keypad for the next pressed key.

    def verify_login(self):
        #Check that the password just entered via the keypad matches that in the password file.
        #Store the result (Y or N) in the override-signal.
        # Also, this should call the LED Board to initiate the appropriate lighting pattern for login success or failure.
        pass

    def validate_passcode_change(self):
        #Check that the new password is legal. If so, write the new password in the password file.
        # A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
        # As in verify login, this should use the LED Board to signal success or failure in changing the password
        pass

    def light_one_led(self,nr):
        print("Lighting led nr: ", nr, end = " ")
        print("det funka!!")
        #Using values stored in the Lid and Ldur slots, call the LED Board and request that LED
        #Lid be turned on for Ldur seconds.

        pass

    def flash_leds(self):
        print("ALL LEDS ARE FLASHING")
        #Call the LED Board and request the flashing of all LEDs.
        pass

    def twinkle_leds(self):
        print("ALL LEDS ARE TWINKLING")
        #Call the LED Board and request the twinkling of all LEDs.
        pass

    def exit_action(self):
        print("POWERING DOWN!")
        #Call the LED Board to initiate the power down lighting sequence.
        pass

    def read_to_active(self):
        print("inni read to active - test 2")
        self.twinkle_leds()
        self.reset_cump()

    def reset_cump(self):
        print("resets CUMP")
        self.fsm.CUMP = ""

    def add_to_cump(self):

        self.fsm.CUMP += self.get_next_signal()
        print("adds to cump - test 3")

    def read_wrong_nr(self):
        print("inside read wrong nr - test 4")
        self.flash_leds()
        self.reset_cump()

    def power_down(self):
        print("inside power down")
        self.light_led_2()
        self.light_led_4()
        self.light_led_6()

    def flash_change_state(self):
        print("Change of state flash")
        self.light_led_1()
        self.light_led_2()

    def add_to_dp(self):
        print("add to DP")
        self.fsm.DP += self.fsm.signal

    def reset_dp(self):
        print("reset DP")
        self.fsm.DP = ""

    def reset_dp_cump(self):
        print("reset DP & CUMP")
        self.reset_cump()
        self.reset_dp()

    def pr2_to_active(self):
        print("go from pr2 to active")
        self.reset_dp_cump()
        self.flash_leds()

    def verify_to_active(self):
        print("go from verify to active")
        self.twinkle_leds()
        self.fsm.CP = self.fsm.DP
        self.reset_dp_cump()

    def light_led_1(self):
        self.light_one_led(p1)
        print("inni light led 1")

    def light_led_2(self):
        self.light_one_led(p2)
        print("inni light led 2")

    def light_led_3(self):
        self.light_one_led(p3)
        print("inni light led 3")

    def light_led_4(self):
        self.light_one_led(p4)
        print("inni light led 4")

    def light_led_5(self):
        self.light_one_led(p5)
        print("inni light led 5")

    def light_led_6(self):
        self.light_one_led(p6)
        print("inni light led 6")

    #kjorer kode for å teste
    def main(self):
        self.init_rules()
        self.fsm.run_rules()

#lager et objekt og kjorer main for å teste rules
kpcObject = KPC()
kpcObject.main()