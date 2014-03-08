import sys,serial

ARDUINO_LOCATION =  "/dev/ttyACM0"
BAUD_RATE = 9600
# ser = serial.Serial(ARDUINO_LOCATION,BAUD_RATE)

def send(char):
    print "sending " + char
    # try:
        # char is an arbitrarily defined etter code sent to the arduino
        # ser.write(char)
    # except:
        # return "Unexpected error:", sys.exc_info()[0]

def buzz():
    send("H")
    return "Buzzed"

def unlock():
    send("J")
    return "Unlocked"

def lock():
    send("I")
    return "Locked"
