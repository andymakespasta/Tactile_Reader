import serial, time,

def connect(protocol):
    ser= serial.Serial(GS.Settings['ComPort'], 9600, timeout=5)
    time.sleep(1) #give the connection a second to settle
    if ser.isOpen():
        while True:
        data = arduino.readline()
        data = data.rstrip('\n')
        print(data)
        print(protocol)
        if data != protocol:
            print("protocol mismatch--are you sure this is the right port/device?")
    else:
        print("openfail")
        #remember to tweak the arduino side code


def serial_send(port,power):
    port = port % 256
    power = power % 256
    ser.write(bytes((port,)),bytes((power,))) # prefix b is required for Python 3.x, optional for Python 2.x
 







ser= serial.Serial(GS.Settings['ComPort'], 9600)
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
 """
 >>> import serial
>>> ser = serial.Serial('/dev/tty.usbserial', 9600)
>>> while True:
...     print ser.readline()
'1 Hello world!\r\n'
'2 Hello world!\r\n'
'3 Hello world!\r\n'

Writing data to Arduino is easy too (the following applies to Python 2.x):

>>> import serial # if you have not already done so
>>> ser = serial.Serial('/dev/tty.usbserial', 9600)
>>> ser.write('5')

In Python 3.x the strings are unicode by default. When sending data to Arduino, they have to be converted to bytes. This can be done by prefixing the string with b:

>>> ser.write(b'5') # prefix b is required for Python 3.x, optional for Python 2.x



---------------------------------
>>> import serial
>>> ser = serial.Serial(0)  # open first serial port
>>> print ser.name          # check which port was really used
>>> ser.write("hello")      # write a string
>>> ser.close()             # close port



>>> ser = serial.Serial('/dev/ttyS1', 19200, timeout=1)
>>> x = ser.read()          # read one byte
>>> s = ser.read(10)        # read up to ten bytes (timeout)
>>> line = ser.readline()   # read a '\n' terminated line
>>> ser.close()




>>> ser = serial.Serial(1, 38400, timeout=0,
...                     parity=serial.PARITY_EVEN, rtscts=1)
>>> s = ser.read(100)       # read up to one hundred bytes
...                         # or as much is in the buffer


>>> ser = serial.Serial()
>>> ser.baudrate = 19200
>>> ser.port = 0
>>> ser
Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
>>> ser.open()
>>> ser.isOpen()
True
>>> ser.close()
>>> ser.isOpen()
False
-----------------------------------------------------
import serial
connected = False
ser = serial.Serial("COM11", 9600)

while not connecte:
  serin = ser.read()
  connected = True

ser.write("1")

----arduino side------

setup(){
Serial.begin(9600);
pinMode(13,OUTPUT);
Serial.write('1');
}

loop(){
  if (Serial.available() > 0){//if data present

------------------------------------------------------

------serial port finder-----
import sys
import glob
import serial


def serial_ports():
    """Lists serial ports

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())
}







python -m serial.tools.list_ports will print a list of available ports. It is also possible to add a regexp as first argument and the list will only include entries that matched.


pySerial includes a small console based terminal program called Miniterm. It ca be started with python -m serial.tools.miniterm <port name> (use option -h to get a listing of all options).