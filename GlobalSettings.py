"""Global Settings is a container for Global Settings and reads json"""
import json
import os

def save_settings():
    f = open('settings.json','w')
    f.write(json.dumps(Settings, sort_keys=True, indent=2, separators=(',', ': ')))
    f.close()


#imports user settings and creates default if no file
try:
    f = open('settings.json','r')
    Settings = json.load(f)
    f.close()
except IOError:
    f = open('settings.json','w')
    from string import ascii_uppercase
    Settings = {
        'file_folder': "txt_files\\",#list of all characters used
        'encoding': "UTF-8",
        'letter_delay': 300, #in ms
        'word_delay':   500, #added to letter_delay
        'language_folder': "languages",
        'languages': [
            'english',
            'numbers'
            ]#these should be modules found in directory, and earlier ones will take precedence
    }
    f.write(json.dumps(Settings, sort_keys=True, indent=2, separators=(',', ': ')))
    f.close()


#holds global settings which are not changed during execution
version = "0.4"

#this line removes file, settings will not be saved and defaults used
os.remove('settings.json')


#GS.Settings['encoding'], is how to use the variables
#GS.