"""loads and parses text file into giant list"""
import os
import GlobalSettings as GS


class FileLoader():
    def __init__(self):
        try:
            self.f = open( GS.Settings["file_folder"]+"welcome.txt", "r", encoding=GS.Settings['encoding'])
        except FileNotFoundError:
            if not os.path.exists( GS.Settings["file_folder"] ):
                os.makedirs( GS.Settings["file_folder"] )
            self.f = open( GS.Settings["file_folder"]+"welcome.txt", "w+", encoding=GS.Settings['encoding'])
            self.f.write("Serial_Reader_V"+GS.version)
            self.f.seek(0,0)
        self.text_file=[]
        lines = self.f.readlines()
        for line in lines:
            thisline = line.split(" ")
            for word in thisline:
                self.text_file.append(word)
        #print(self.text_file)

    def load_file(self, filename):
        try:
            ftemp = open(filename, "r", encoding=GS.Settings['encoding'])
            self.f.close()
            self.f = ftemp
        except FileNotFoundError:
            try: 
                ftemp = open(GS.Settings["file_folder"]+filename, "r", encoding=GS.Settings['encoding'])
                self.f.close()
                self.f = ftemp
            except FileNotFoundError:
                print("File Not Found!!!")
        self.f.seek(0,0)
        self.text_file=[]
        lines = self.f.readlines()
        for line in lines:
            thisline = line.split(" ")
            for word in thisline:
                self.text_file.append(word)
        #print(self.text_file)

    def get_file_wordcount(self):
        return len(self.text_file)

if __name__ == "__main__":

    fileloader = FileLoader()
    fileloader.load_file("WarAndPeace.txt")
    print (fileloader.get_file_wordcount())
    print (fileloader.text_file[106])