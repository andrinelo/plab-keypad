import RPi.GPIO as GPIO
import time

#Keypad - interface to the physical keypad
class Keypad:

    #hvordan connecte R og C
    #hva skal vare i listen med rowpins og columnpins?
    def __init__(self):

        self.rowpins = [18,23,24,25] #list of rowpins?
        self.columnpins= [17,27,22  ] #list of columnpins
        self.setup()


    def setup(self):

        #Set the proper mode via:
        print("Setting mode anf rows and cols")
        GPIO.setmode(GPIO.BCM)
        rad = self.rowpins
        cols = self.columnpins
        print("Have set mode anf rows and cols")

        #sets the row pins as outputs
        for rp in rad:
            print("Rowpin: ", rp)
            GPIO.setup(rp,GPIO.OUT)

        #sets the column pins as inputs
        for cp in cols:
            print("Colpin: ", cp)
            GPIO.setup(cp, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


    def do_polling(self):
        #Use nested loops (discussed above) to determine
        #the key currently being pressed on the keypad.
        location = None

        for rp in self.rowpins:
            GPIO.output(rp, GPIO.LOW)

        for rp in self.rowpins:
            #setting the RP to HIGH one at a time
           # print("in do pollig: rp = ", rp)
            GPIO.output(rp,GPIO.HIGH)

            #looping through columns
            for cp in self.columnpins:
              #  print("in do pollig: cp = ", cp)

                #check to see if column is HIGH
                #20 times with delay to make sure its correct

                count = 0
                for i in range(0,20):
                    if GPIO.input(cp) == GPIO.HIGH:
                        count += 1
                    time.sleep(0.01)

                if count == 20:
                    radplass = self.rowpins.index(rp)
                    colplass = self.columnpins.index(cp)
                    # the key being pressed
                    location = (radplass, colplass)
                    if location:
                        GPIO.output(rp, GPIO.LOW)
                        return location

            GPIO.output(rp, GPIO.LOW)

    #    return location

    def get_next_signal(self):
        while True:
            pair = self.do_polling()
            if pair:
                sign = (pair[0]*3) + pair[1] + 1
                if sign == 10:
                    sign = "*"
                elif sign == 11:
                    sign = "0"
                elif sign == 12:
                    sign = "#"
                else: sign = str(sign)
                return sign
'''
if __name__ == '__main__':
    keypad = Keypad()
    while True:
        sign = keypad.get_next_signal()
        print("Signal = ", sign)
'''

            # skal gjøre polling
            # self
        #This is the main interface between the agent and the keypad.
        #It should initiate repeated calls to do polling until a key press is detected.

