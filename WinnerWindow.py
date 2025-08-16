from tkinter import *
from tkinter import font as tkfont
import sys
class Window:
    def __init__(self,number):
        self.number=number+1
        self.CreateWindow()
        self.CreateLabels()
        self.Mainloop()
    def CreateWindow(self):
        self.winnerwindow=Tk()
        self.winnerwindow.geometry("900x600+500+200")
        self.winnerwindow.title("Sikrmish Of Tank Officers - Welcome")
        self.winnerwindow.resizable(False, False)
        self.winnerwindow.configure(bg="#252423")
        self.winnerwindow.overrideredirect(True)
    def CreateLabels(self):
        my_font = tkfont.Font(family="Helvetica", size=24) 
        if self.number != 0:
            label=Label(self.winnerwindow, text=f"WINNER is player number: {self.number}",font=my_font, fg="white", bg="#252423")
        else:
            label=Label(self.winnerwindow, text=f"there is no winner",font=my_font, fg="white", bg="#252423")
        label.place(relx=0.5,rely=0.5,anchor="center")
    def KillYourSelf(self):
        self.winnerwindow.quit()
        return
    def Mainloop(self):
        self.winnerwindow.after(3000,self.KillYourSelf)
        self.winnerwindow.mainloop()
