import Beta0_1SOTO
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
class WelcomeScreen:
    def __init__(self):
        self.CreateMainWidow()
        self.CreateButtons()
        self.window.mainloop()
    def CreateMainWidow(self):
        self.window = tk.Tk()
        self.window.geometry("900x600")
        self.window.title("Sikrmish Of Tank Officers - Welcome")
        self.window.resizable(False, False)
        self.window.config(bg="#252423")

    def CreateButtons(self):
        self.ButtonFont = tkfont.Font(family="Impact", size=12)
        StartButton = tk.Button(self.window, text="Start", width=25, height=4, font=self.ButtonFont, bg="#7C7976", command=self.StartGame,)
        ControlsButton = tk.Button(self.window, text="Controls", width=25, height=4, font=self.ButtonFont, command=self.OpenControlsWindow, bg="#7C7976")
        QuitButton = tk.Button(self.window, text="Quit", width=25, height=4, font=self.ButtonFont, command=self.window.quit, bg="#7C7976")
        StartButton.place(relx=0.5, y=150, anchor="center")
        ControlsButton.place(relx=0.5, y=250, anchor="center")
        QuitButton.place(relx=0.5, y=350, anchor="center")

    def StartGame(self):
        NumberOfPlayers=3
        KeyBinds = [["W", "A", "S", "D", "SPACE"], ["I", "J", "K", "L", "P"], ["T", "F", "G", "H", "Z"]]
        game=Beta0_1SOTO.Game(NumberOfPlayers,KeyBinds)
        game.GameLoop()

    def UserNotDumb(self):
        for i in range(len(self.keybind)):
            CurrentList=self.keybind[i]
            if self.controls_1 != self.controls_1:
                messagebox.showerror("Fatal error","Error is located one meters from the monitor.")
                print(self.controls_1)
                print(CurrentList)
            elif self.controls_2!=CurrentList:
                messagebox.showerror("Fatal error ","Error is located one meters from the monitor.")

            elif self.controls_3!=CurrentList:
                messagebox.showerror("Fatal error ","Error is located one meters from the monitor.")

            elif self.controls_4!=CurrentList:
                messagebox.showerror("Fatal error ","Error is located one meters from the monitor.")

            elif self.controls_5!=CurrentList:
                messagebox.showerror("Fatal error ","Error is located one meters from the monitor.")

            elif self.controls_6!=CurrentList:
                messagebox.showerror("Fatal error ","Error is located one meters from the monitor.")

            else:
                self.window.destroy()
        #dont mind this its still in progress

    def ProceedToControls(self):
        self.OpenControlsWindow()

    def OpenControlsWindow(self):
        self.controls_window = tk.Toplevel(self.window)
        self.controls_window.geometry("900x600")
        self.controls_window.title("Controls")
        self.controls_window.resizable(False, False)
        self.controls_window.config(bg="#252423")
        
        Label = tk.Label(self.controls_window, text="CONTROLS", font=tkfont.Font(family="Arial", size=40), fg="white", bg="#252423")
        Label.place(x=315,y=50)
        Label_1 = tk.Label(self.controls_window, text="first player:", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_1.place(x=305,y=135)
        self.controls_input_1=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_1.place(x=450,y=140)
        self.controls_input_1.insert(0, "W/A/S/D/E")

        Label_2 = tk.Label(self.controls_window, text="second player:", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_2.place(x=305,y=170)
        self.controls_input_2=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_2.place(x=450,y=175)
        self.controls_input_2.insert(0, "T/F/G/H/Z")

        Label_3 = tk.Label(self.controls_window, text="third player:", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_3.place(x=305,y=205)
        self.controls_input_3=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_3.place(x=450,y=210)
        self.controls_input_3.insert(0, "I/J/K/L/O")

        Label_4 = tk.Label(self.controls_window, text="fourth player:", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_4.place(x=305,y=240)
        self.controls_input_4=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_4.place(x=450,y=245)
        self.controls_input_4.insert(0, "Y/X/C/V/Q")

        Label_5 = tk.Label(self.controls_window, text="fifth player:", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_5.place(x=305,y=275)
        self.controls_input_5=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_5.place(x=450,y=280)
        self.controls_input_5.insert(0, "B/N/M/SPACE/R")

        Label_6 = tk.Label(self.controls_window, text="sixth player:", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_6.place(x=305,y=315)
        self.controls_input_6=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_6.place(x=450,y=320)
        self.controls_input_6.insert(0, "P/P/P/P/P")#key arrows

        self.keybind=[]
        self.controls_1=self.controls_input_1.get().split("/")
        self.keybind.append(self.controls_1)
        self.controls_2=self.controls_input_2.get().split("/")
        self.keybind.append(self.controls_2)
        self.controls_3=self.controls_input_3.get().split("/")
        self.keybind.append(self.controls_3)
        self.controls_4=self.controls_input_4.get().split("/")
        self.keybind.append(self.controls_4)
        self.controls_5=self.controls_input_5.get().split("/")
        self.keybind.append(self.controls_5)
        self.controls_6=self.controls_input_6.get().split("/")
        self.keybind.append(self.controls_6)
        print(self.keybind)
        CloseButton = tk.Button(self.controls_window, text="Close", font=tkfont.Font(family="Impact", size=12), command=self.UserNotDumb, bg="#7C7976")
        CloseButton.place(x=420,y=550)

WelcomeScreen()