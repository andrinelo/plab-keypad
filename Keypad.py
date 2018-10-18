import RPi.GPIO as GPIO
import time

#Keypad - interface to the physical keypad
class Keypad():

    #hvordan connecte R og C
    #hva skal vare i listen med rowpins og columnpins?


    def setup(self):
        rowpins = [0,1,2,3] #list of rowpins?
        columnpins= [0,1,2] #list of columnpins

        #Set the proper mode via:
        GPIO.setmode(GPIO.BCM)

        #sets the row pins as outputs
        for rp in rowpins:
            GPIO.setup(rp,GPIO.OUT)

        #sets the column pins as inputs
        for cp in columnpins:
            GPIO.setup(cp, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        return 0

    def do_polling(self):
        #Use nested loops (discussed above) to determine
        #the key currently being pressed on the keypad.
        location = None

        for rp in range(0,4):
            #setting the RP to HIGH one at a time
            GPIO.output(rp,GPIO.HIGH)

            #looping through columns
            for cp in range(0,3):
                #check to see if column is HIGH
                #20 times with delay to make sure its correct

                count = 0
                for i in range(0,20):
                    if GPIO.input(cp) == GPIO.HIGH:
                        count += 1
                    time.sleep(20)

                if count == 20:
                    # the key being pressed
                    location = (rp, cp)

            GPIO.output(rp, GPIO.low)

        return location

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


            # skal gjøre polling
            # self
        #This is the main interface between the agent and the keypad.
        #It should initiate repeated calls to do polling until a key press is detected.

