import serial

ser= serial.Serial('/dev/tty.usbserial', 9600)

arduino = serial.Serial('COM1', 115200, timeout=.1)

import serial, time
arduino = serial.Serial('COM1', 115200, timeout=.1)
time.sleep(1) #give the connection a second to settle
arduino.write("Hello from Python!")
while True:
	data = arduino.readline()
	if data:
		print data.rstrip('\n') #strip out the new lines for now
		# (better to do .read() in the long run for this reason



connected = False

arduino = serial.Serial('COM1', 115200)

while not connected:
	serin = ser.read() #this is blocking
	connected = True


print("it gets better")


