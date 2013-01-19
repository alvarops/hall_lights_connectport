import serial
serialport = serial.Serial("/dev/ttyO1", 9600, timeout=0.5)
serialport.write("Q")
response = serialport.readlines(None)
print response
