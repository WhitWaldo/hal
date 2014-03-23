import sys,serial
import settings

BAUD_RATE = 9600
ser = serial.Serial(settings.ARDUINO_LOCATION, BAUD_RATE)

def send(char):
    print("sending" + char)
    try:
        # char is an arbitrarily defined letter code sent to the arduino
        ser.write(char)
    except:
        return "Unexpected error:", sys.exc_info()[0]

def buzz():
    send("H")
    return "Buzzed"

def unlock():
    send("J")
    return "Unlocked"

def lock():
    send("I")
    return "Locked"
