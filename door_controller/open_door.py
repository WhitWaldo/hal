import serial
ARDUINO_LOCATION =  "/dev/ttyACM0"
BAUD_RATE = 9600
ser = serial.Serial(ARDUINO_LOCATION,BAUD_RATE)
#This is totally abritrary but the serial listener on the arduino is listening for an "H" or the ASCII value 97 for it to trigger the open command
ser.write("H")
