"""tkinter GUI for SerialReader"""
import tkinter as Tk

class GUI():
    def __init__(self):
        self.display_font = ('Helvetica', 30, 'bold')
        file_len = 1024
        Name = "Serial Reader V0.4"

        self.root = Tk.Tk()

        #root.title(Name)

        play_icon = Tk.PhotoImage(file="icons\play.gif")
        pause_icon = Tk.PhotoImage(file="icons\pause.gif")
        next_icon = Tk.PhotoImage(file="icons\\next.gif")
        prev_icon = Tk.PhotoImage(file="icons\prev.gif")

        #this section is the place where the text is displayed
        self.word_display = Tk.Frame(self.root, width=40, height=10)
        welcome_text = Tk.Label(self.word_display, bd=0, padx=0, font=self.display_font, fg="black", text=Name)
        welcome_text.pack()

        #this section is the control bar and prev/play/pause/next buttons
        control_bar = Tk.Frame(self.root, padx=10, pady=3)
        self.prev_button = Tk.Button(control_bar, text="prev", image=prev_icon, bd=0, command = self.prev_button_click)
        self.play_button = Tk.Button(control_bar, text="play", image=play_icon, bd=0, command = self.play_button_click)
        self.pause_button = Tk.Button(control_bar,text="pause",image=pause_icon,bd=0, command = self.pause_button_click)#, state=Tk.DISABLED
        self.next_button = Tk.Button(control_bar, text="next", image=next_icon, bd=0, command = self.next_button_click)
        self.progress_slider = Tk.Scale(control_bar, orient=Tk.HORIZONTAL, showvalue=0, from_=0, to=file_len, length=500)
        self.prev_button.grid(row=0, column=1)
        self.play_button.grid(row=0, column=2)
        self.next_button.grid(row=0, column=3)
        self.progress_slider.grid(row=0, column=5)
        print("cheese")
        #gridding up main window
        self.word_display.grid(row=2, column=11)
        control_bar.grid(row=3, column=11)
        self.root.columnconfigure(11, weight=1, minsize=500)
        self.root.rowconfigure(2, weight=1, minsize=100, pad=10)
        self.root.rowconfigure(3, weight=0, minsize=10, pad=10)

        self.root.mainloop()


    def display_word(self,string,n):#highlights nth char, 0 or >strlen no lighlight
        for child in self.word_display.winfo_children():
            child.destroy()
        if (n <= 0 or n > len(string)):
            text = Tk.Label(word_display, bd=0, padx=0, font=display_font, 
                            fg="black", text=string)
            text.pack()
        else :
            text_front= Tk.Label(self.word_display, bd=0, padx=0, font=self.display_font, 
                                 fg="black", text=string[0:n-1])
            text_hilit= Tk.Label(self.word_display, bd=0, padx=0, font=self.display_font, 
                                 fg="red", text=string[n-1])
            text_back = Tk.Label(self.word_display, bd=0, padx=0, font=self.display_font, 
                                 fg="black", text=string[n:len(string)])
            text_front.grid(row=0,column=1)
            text_hilit.grid(row=0,column=2)
            text_back.grid(row=0, column=3)

    def play_button_click(self):
        self.play_button.grid_remove()
        self.pause_button.grid(row=0, column=2)
        self.display_word("Yeah Baby!",3)

    def pause_button_click(self):
        self.pause_button.grid_remove()
        self.play_button.grid(row=0, column=2)

    def next_button_click(self):
        print ("next")

    def prev_button_click(self):
        print ("prev")

if __name__ == "__main__":

    root = GUI()
    print("cheese")
    root.root.mainloop()










# class GUI(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         fr = Frame(self)
#         fr.pack()
#         self.canvas  = Canvas(fr, height = 100, width = 100)
#         self.canvas.pack()
#         self.rect = self.canvas.create_rectangle(25, 25, 75, 75, fill = "white")
#         self.do_blink = False
#         start_button = Button(self, text="start blinking", 
#                               command=self.start_blinking)
#         stop_button = Button(self, text="stop blinking", 
#                               command=self.stop_blinking)
#         start_button.pack()
#         stop_button.pack()



#     def start_blinking(self):
#         self.do_blink = True
#         self.blink()

#     def stop_blinking(self):
#         self.do_blink = False

#     def blink(self):
#         if self.do_blink:
#             current_color = self.canvas.itemcget(self.rect, "fill")
#             new_color = "red" if current_color == "white" else "white"
#             self.canvas.itemconfigure(self.rect, fill=new_color)
#             self.after(1000, self.blink)