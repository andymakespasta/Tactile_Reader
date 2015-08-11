import serial
import GlobalSettings as GS
#import bluetooth
try:
    if GS.Settings['ComMode'] == "USB":
        from USBSerialSend import *
    if GS.Settings['ComMode'] == "Bluetooth":
        from BTSerialSend import *
except KeyError:
    GS.Settings['ComMode'] = "USB"
    print("assuming USB connection")
    from USBSerialSend import *
    GS.save_settings()

#simply import this, and use the following commands
#Connect("pp5x4")
#SerialSend(port,power)



#ser = serial.Serial(GS.Settings['port'],19200)#which baud rates














"""
A simple Python script to send messages to a sever over Bluetooth 
using PyBluez (with Python 2).
"""
"""
import bluetooth

serverMACAddress = '00:1f:e1:dd:08:3d'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
sock.close()
"""
"""
import socket

serverMACAddress = '00:1f:e1:dd:08:3d'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()





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
"""