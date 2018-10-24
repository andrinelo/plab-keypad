#KPC - the keypad controller agent that coordinates activity between the other 3 classes along with veryifying and changing passwords
from FSM import FSM
from Keypad import Keypad
from FSMRule import FSMRule
from LedBoard import LedBoard

p1 = 2
p2 = 4
p3 = 7
p4 = 8
p5 = 10
p6 = 12

class KPC:


    def __init__(self):
        self.keypad = Keypad()
        self.fsm = FSM(self)
        self.ledboard = LedBoard()
        self.override_signal = None
        self.bulbNumber = "" #which bulb to be lit, LID
        self.ledTime = "" #duration of lit LED, Ldur

    def init_rules(self):
        self.fsm.add_rule("S-INIT", "S-READ", self.fsm.activate_is_true, self.ledboard.power_up)

        self.fsm.add_rule("S-READ", "S-ACTIVE", self.fsm.validate_entire, self.read_to_active)
        self.fsm.add_rule("S-READ", "S-READ", self.fsm.validate_cump, self.add_to_cump)
        self.fsm.add_rule("S-READ", "S-READ", self.fsm.unvalidate_cump, self.read_wrong_nr)
        self.fsm.add_rule("S-READ", "S-INIT", "#", self.ledboard.power_down)

        self.fsm.add_rule("S-ACTIVE", "S-INIT", "#", self.ledboard.power_down)
        self.fsm.add_rule("S-ACTIVE", "S-LED", "1", self.bulb2beLIT)
        self.fsm.add_rule("S-ACTIVE", "S-LED", "2", self.bulb2beLIT)
        self.fsm.add_rule("S-ACTIVE", "S-LED", "3", self.bulb2beLIT)
        self.fsm.add_rule("S-ACTIVE", "S-LED", "4", self.bulb2beLIT)
        self.fsm.add_rule("S-ACTIVE", "S-LED", "5", self.bulb2beLIT)
        self.fsm.add_rule("S-ACTIVE", "S-LED", "6", self.bulb2beLIT)
        self.fsm.add_rule("S-ACTIVE", "S-PR1", "*", self.flash_change_state)

        self.fsm.add_rule("S-LED", "S-TIME", "*", None) #ingenting skjer?
        self.fsm.add_rule("S-LED", "S-INIT", "#", self.ledboard.power_down)

        self.fsm.add_rule("S-TIME", "S-TIME", self.fsm.signal_is_digit, self.add_to_LEDtime)
        self.fsm.add_rule("S-TIME", "S-ACTIVE", "*", self.activate_bulb)
        self.fsm.add_rule("S-TIME", "S-INIT", "#", self.ledboard.power_down)

        self.fsm.add_rule("S-PR1", "S-PR1", self.fsm.signal_is_digit, self.add_to_dp)
        #kommentar under gjelder linje 41
        # noe feil med signal_is_digit, bare prøv å kjøre den som signal og riktig state, og se på feilmeldingen om
        #at: expected string but function found

        #self.fsm.add_rule("S-PR1", "S-ACTIVE", "#", self.reset_dp) - trenger vi denne?
        self.fsm.add_rule("S-PR1", "S-PR2", "*", self.flash_change_state)
        self.fsm.add_rule("S-PR1", "S-INIT", "#", self.ledboard.power_down)

        self.fsm.add_rule("S-PR2", "S-ACTIVE", "#", self.reset_dp_cump)
        self.fsm.add_rule("S-PR2", "S-PRVERIFY", self.fsm.validate_entire_pr, self.flash_change_state)
        self.fsm.add_rule("S-PR2", "S-PR2", self.fsm.validate_cump_pr, self.add_to_cump)
        #gjelder linje 50; får ikke testet uten GPIO som ikke går uten RPi
        self.fsm.add_rule("S-PR2", "S-ACTIVE", self.fsm.unvalidate_cump_pr, self.pr2_to_active)
        self.fsm.add_rule("S-PR2", "S-INIT", "#", self.ledboard.power_down)

        self.fsm.add_rule("S-PRVERIFY", "S-ACTIVE", "*",  self.verify_to_active)
        self.fsm.add_rule("S-PRVERIFY", "S-INIT", "#", self.ledboard.power_down)

        self.fsm.add_rule("S-ACTIVE", "S-INIT", "#", self.ledboard.power_down)

    #def init_passcode_entry(self):
        #Clear the passcode-buffer and initiate a power up lighting sequence on the LED Board.
        # This should be done when the user first presses the keypad.
        #self.main()


    def activate_bulb(self):
        self.ledboard.light_led(int(self.bulbNumber), int(self.ledTime))
        self.bulbNumber = ""
        self.ledTime = ""


    def add_to_LEDtime(self):
        self.ledTime += self.fsm.signal

    def bulb2beLIT(self):
        self.bulbNumber = self.fsm.signal

    def get_next_signal(self):
        if self.override_signal:
            print("Finner bare overrideSignal")
            return self.override_signal
        else:
            print("Signal hentet til KPC")
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


    def read_to_active(self):
        print("inni read to active - test 2")
        self.ledboard.twinkle_all_leds()
        self.reset_cump()

    def reset_cump(self):
        print("resets CUMP")
        self.fsm.CUMP = ""

    def add_to_cump(self):
        self.fsm.CUMP += self.fsm.signal
        print("adds to cump - test 3")

    def read_wrong_nr(self):
        print("inside read wrong nr - test 4")
        self.ledboard.flash_all_leds()
        self.reset_cump()

    def flash_change_state(self):
        print("Change of state flash")
        self.ledboard.light_led(3, 1)
        self.ledboard.light_led(4, 1)

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
        self.ledboard.flash_all_leds()
    def verify_to_active(self):
        print("go from verify to active")
        self.ledboard.twinkle_all_leds()
        self.fsm.CP = self.fsm.DP
        self.reset_dp_cump()

    def power_down(self):
        self.ledboard.power_down()
        self.__init__() #to reset all states in KPC and FSM


    #kjorer kode for å teste
    def main(self):
        self.init_rules()
        self.fsm.main_loop()

if __name__ == "__main__":
    kpc = KPC()
    kpc.main()


#lager et objekt og kjorer main for å teste rules
#kpcObject = KPC()
#kpcObject.main()