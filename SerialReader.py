"""reads text to display and send through serial port sequentially"""
#program displays using Tkinter, and sends data to arduino.
#A file is shown word by word, with current letter highlighted.
import tkinter as Tk



def display_word(string,n):#highlights nth char, 0 or >strlen no lighlight
    for child in word_display.winfo_children():
        child.destroy()
    if (n <= 0 or n > len(string)):
        text = Tk.Label(word_display, bd=0, padx=0, font=display_font, 
                        fg="black", text=string)
        text.pack()
    else :
        text_front= Tk.Label(word_display, bd=0, padx=0, font=display_font, 
                             fg="black", text=string[0:n-1])
        text_hilit= Tk.Label(word_display, bd=0, padx=0, font=display_font, 
                             fg="red", text=string[n-1])
        text_back = Tk.Label(word_display, bd=0, padx=0, font=display_font, 
                             fg="black", text=string[n:len(string)])
        text_front.grid(row=0,column=1)
        text_hilit.grid(row=0,column=2)
        text_back.grid(row=0, column=3)



def play_button_click():
    play_button.grid_remove()
    pause_button.grid(row=0, column=2)
    display_word("Yeah Baby!",3)


def pause_button_click():
    pause_button.grid_remove()
    play_button.grid(row=0, column=2)

def next_button_click():
    print ("next")

def prev_button_click():
    print ("prev")



display_font = ('Helvetica', 30, 'bold')
file_len = 1024
Name = "Serial Reader V0.4"

root = Tk.Tk()
root.title(Name)


play_icon = Tk.PhotoImage(file="icons\play.gif")
pause_icon = Tk.PhotoImage(file="icons\pause.gif")
next_icon = Tk.PhotoImage(file="icons\\next.gif")
prev_icon = Tk.PhotoImage(file="icons\prev.gif")

#this section is the place where the text is displayed
word_display = Tk.Frame(root, width=40, height=10)
welcome_text = Tk.Label(word_display, bd=0, padx=0, font=display_font, 
                        fg="black", text=Name)
welcome_text.pack()

#this section is the control bar and prev/play/pause/next buttons
control_bar = Tk.Frame(root, padx=10, pady=3)
prev_button = Tk.Button(control_bar, text="prev", image=prev_icon, bd=0, command = prev_button_click)
play_button = Tk.Button(control_bar, text="play", image=play_icon, bd=0, command = play_button_click)
pause_button = Tk.Button(control_bar,text="pause",image=pause_icon,bd=0, command = pause_button_click)#, state=Tk.DISABLED
next_button = Tk.Button(control_bar, text="next", image=next_icon, bd=0, command = next_button_click)
progress_slider = Tk.Scale(control_bar, orient=Tk.HORIZONTAL, showvalue=0, from_=0, to=file_len, length=500)
prev_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
next_button.grid(row=0, column=3)
progress_slider.grid(row=0, column=5)




#gridding up main window
word_display.grid(row=2, column=11)
control_bar.grid(row=3, column=11)
root.columnconfigure(11, weight=1, minsize=500)
root.rowconfigure(2, weight=1, minsize=100, pad=10)
root.rowconfigure(3, weight=0, minsize=10, pad=10)

root.mainloop()

#TKdocs is a good resource

#button.configure() could output all options!?!

# from tkinter import *
# from tkinter import ttk
# # root = Tk()
# l =ttk.Label(root, text="Starting...")
# l.grid()
# l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
# l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
# l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
# root.mainloop()


# # create a canvas with no internal border
# canvas = Canvas(bd=0, highlightthickness=0)
# canvas.pack(fill=BOTH, expand=1)

# # track changes to the canvas size and draw
# # a rectangle which fills the visible part of
# # the canvas

# def configure(event):
#     canvas.delete("all")
#     w, h = event.width, event.height
#     xy = 0, 0, w-1, h-1
#     canvas.create_rectangle(xy)
#     canvas.create_line(xy)
#     xy = w-1, 0, 0, h-1
#     canvas.create_line(xy)

# canvas.bind("<Configure>", configure)

# mainloop()
