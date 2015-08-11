import serial, time, threading

#globals
check_input_wait = 0 #0 for never check

#this is the actual sending function
def port_power(port, power):   
    ser.write(bytes([port%256])) # prefix b is required for Python 3.x, optional for Python 2.x
    ser.write(bytes([power%256]))


#this function checks messages from the board, see global check_input_wait
def check_input():
    if(ser.inWaiting()>0):

    if check_input_wait != 0:#it uses a timer thread to repeatedly call itself
        check_thread.start()





#tries the first ports for an active port
port=0
while port < 10:
    try:
        ser = serial.Serial(port,9600,timeout=5)
    except:
        if port > 10:
            sys.exit()
        else:
            port = port + 1
print (ser.name) #this is the port name to save to settings in case

if check_input_wait != 0:
    check_thread = threading.Timer(check_input_wait,check_input)



while True:
    print("bump")
    port_power(0,8)
    time.sleep(1)
    data = ser.readline()
    print(data)

    port_power(1,7)
    time.sleep(1)
    data = ser.readline()
    print(data)

