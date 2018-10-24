import RPi.GPIO as GPIO
import time

#Keypad - interface to the physical keypad
class Keypad:

    #hvordan connecte R og C
    #hva skal vare i listen med rowpins og columnpins?
    def __init__(self):

        self.rowpins = [18,23,24,25] #list of rowpins?
        self.columnpins= [17,27,22  ] #list of columnpins
        self.lastrow_codes = {(3,0): '*', (3,1):'0', (3,2):'#'} #lagt til linje 13
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

    def repeated_match(self,pin,target=GPIO.HIGH, iterations=20, delay=0.01,):
        for i in range(iterations):
            if GPIO.input(pin) != target:
                return False
            time.sleep(delay)
        return True

    def do_polling(self):
        #Use nested loops (discussed above) to determine
        #the key currently being pressed on the keypad.
        #location = None

       # for rp in self.rowpins:
        #    GPIO.output(rp, GPIO.LOW)

        for r,rp in enumerate(self.rowpins):
            #setting the RP to HIGH one at a time
           # print("in do pollig: rp = ", rp)
            GPIO.output(rp,GPIO.HIGH)

            #looping through columns
            for c,cp in enumerate(self.columnpins):
                if self.repeated_match(cp,target=GPIO.HIGH):
                    GPIO.output(rp,GPIO.LOW)
                    return (r,c)
            GPIO.output(rp, GPIO.LOW)
        return None


    def get_next_signal(self):
        while True:
            pair = self.do_polling()
            if pair:
                row = pair[0]
                col = pair[1]
                print("row", row, "col", col)
                if row<3: return str(3*row +(col+1))
                else: return self.lastrow_codes[(row,col)]


if __name__ == '__main__':
    print("Heihei test")
    keypad = Keypad()
    while True:
        sign = keypad.get_next_signal()
        print("Signal = ", sign)

            # skal gjøre polling
            # self
        #This is the main interface between the agent and the keypad.
        #It should initiate repeated calls to do polling until a key press is detected.

