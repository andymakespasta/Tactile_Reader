try:
    f = open("txt_books\Frankenstein.txt", "r")
except FileNotFoundError:
    print("Cannot find file!!!")
print("heyo")
lines = f.readlines();
for line in lines:
    thisline = line.split(" ");
    for word in thisline:
        print(word)
f.close()
