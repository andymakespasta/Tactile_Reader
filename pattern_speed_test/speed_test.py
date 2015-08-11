import json
import random
import serialsend as SSend

#speed here is in /10s, delay is () 10000/speed )ms
#hold is in ms, how long each vibration is held

f = open('strong_dir_patterns.json','r')
pattern = json.load(f)
f.close()

'''
try:
    f = open('stats,json','r')
    Stats = json.load(f)
    f.close()
except IOError:
    Stats = {}
'''

random.seed()
range = len(pattern)


while True:
    print("...................................................")
    #change to SSend.blah
    print(pattern[random.randrange(range)])

    try:
        user_response = input("eXit/correct(Y)/wroNg?")
    except SyntaxError:
        user_response = 'y'
    if user_response.lower() ==  'n':
        print ("wrong")
    elif user_response.lower() == 'x':
        break
    elif user_response.lower() == 'y' or user_response.lower() == '':
        print ("correct")
    else :
        print("next")