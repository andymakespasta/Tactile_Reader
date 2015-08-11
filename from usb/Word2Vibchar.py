"""parse words/letters into characterset of vib patterns and timing"""
import importlib
import GlobalSettings as GS

#setup and loading language modules
#f = open( GS.Settings["language_folder"]+"welcome.txt", "r", encoding=GS.Settings['encoding'])

if not os.path.exists( GS.Settings['language_folder'] ):
    os.makedirs( GS.Settings['language_folder'] )

for lan in GS.Settings['languages']:
    try:
        importlib.import_module(GS.Settings['language_folder'] + '.' + lan)
    except ImportError:
        print("no module named "+lan+", not loaded.")


def Convert(string):
    




if __name__ == "__main__":
    print(GS.Settings['languages'])