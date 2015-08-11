import serial, time, threading

#globals
check_input_wait = 1 #0 for never check

def check_input():
    if(True):
        print("boop")

    if check_input_wait != 0:#it uses a timer thread to repeatedly call itself
        check_thread = threading.Timer(check_input_wait, check_input)
        check_thread.start()


if check_input_wait != 0:
    check_thread = threading.Timer(check_input_wait, check_input)
    check_thread.daemon = True 
    check_thread.start()

while True:
    print(".")
    time.sleep(0.5)

