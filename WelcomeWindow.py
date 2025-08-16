import Beta0_1SOTO
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
class WelcomeScreen:
    def __init__(self):
        self.NumberOfPlayers=2
        self.number_first="2"
        self.keybind=[['W', 'A', 'S', 'D', 'E'], ['I', 'J', 'K', 'L', 'O'], ['T', 'F', 'G', 'H', 'Y'],['arrowUp', 'arrowLeft', 'arrowDown', 'arrowRight', 'P'],  ['X','Z', 'C', 'V', 'Q'], ['N', 'B', 'SPACE', 'M', 'R']]
        self.create=False
        self.create1=False
        self.CreateMainWidow()
        self.CreateButtons()
        self.window.mainloop()
    def CreateMainWidow(self):
        if self.create==False:
            self.window = tk.Tk()
            self.window.geometry("900x600+500+200")
            self.window.title("Sikrmish Of Tank Officers - Welcome")
            self.window.resizable(False, False)
            self.window.config(bg="#252423")
            self.create=True
            self.window.overrideredirect(True)
        else:
            self.controls_window.withdraw()
            self.window.deiconify()
    def CreateButtons(self):
        self.ButtonFont = tkfont.Font(family="Impact", size=12)
        llabel=tk.Label(self.window, text="Skirmish of Tank Officers", font=tkfont.Font(family="Arial", size=40), fg="white", bg="#252423")
        llabel.place(x=170,y=35)
        StartButton = tk.Button(self.window, text="Start", width=25, height=4, font=self.ButtonFont, bg="#7C7976", command=self.StartGame,)
        ControlsButton = tk.Button(self.window, text="Controls", width=25, height=4, font=self.ButtonFont, command=self.OpenControlsWindow, bg="#7C7976")
        QuitButton = tk.Button(self.window, text="Quit", width=25, height=4, font=self.ButtonFont, command=self.window.quit, bg="#7C7976")
        StartButton.place(relx=0.5, y=150, anchor="center")
        ControlsButton.place(relx=0.5, y=250, anchor="center")
        QuitButton.place(relx=0.5, y=350, anchor="center")
    def on_close(self):
        return
    def StartGame(self):
        #KeyBinds = [["W", "A", "S", "D", "E"], ["I", "J", "K", "L", "P"], ["T", "F", "G", "H", "Z"],["N","B","SPACE","M","Q"]]
        Key_binds=self.keybind
        game=Beta0_1SOTO.Game(self.NumberOfPlayers,Key_binds)
        game.GameLoop()

        #dont mind this its still in progres
    def ProceedToControls(self):
        self.OpenControlsWindow()
    def verif(self):
        try:
            self.NumberOfPlayers=int(self.controls_input_7.get())
            if self.NumberOfPlayers>6 or self.NumberOfPlayers<=1:
                return
            else:
                self.CreateMainWidow()
        except:
             messagebox.showerror("Input error", "Please enter a valid number of active players.")
             return
    
    def OpenControlsWindow(self):
        if self.create1==False:
            self.window.withdraw()
            self.controls_window = tk.Toplevel(self.window)
            self.controls_window.geometry("900x600")
            self.controls_window.title("Controls")
            self.controls_window.resizable(False, False)
            self.controls_window.config(bg="#252423")
            self.create1=True
            self.controls_window.protocol("WM_DELETE_WINDOW", self.on_close)
        else:
            self.controls_window.deiconify()
            
        Label = tk.Label(self.controls_window, text="CONTROLS", font=tkfont.Font(family="Arial", size=40), fg="white", bg="#252423")
        Label.place(x=340,y=50)
        Label_user= tk.Label(self.controls_window,text="Keys :",font=tkfont.Font(family="Arial", size=16),fg="white",  bg="#252423")
        Label_user.place(x=280,y=110)
        Label_user_example = tk.Label(self.controls_window, text="UP/LEFT/DOWN/RIGHT/SHOOT",font=tkfont.Font(family="Arial", size=16),fg="white",  bg="#252423")
        Label_user_example.place(x=345,y=110)
        Label_1 = tk.Label(self.controls_window, text="First player :", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_1.place(x=305,y=140)
        self.controls_input_1=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_1.place(x=450,y=140)
        self.controls_input_1.insert(0, "W/A/S/D/E")

        Label_2 = tk.Label(self.controls_window, text="Second player :", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_2.place(x=305,y=170)
        self.controls_input_2=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_2.place(x=450,y=175)
        self.controls_input_2.insert(0, "T/F/G/H/Z")

        Label_3 = tk.Label(self.controls_window, text="Third player :", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_3.place(x=305,y=205)
        self.controls_input_3=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_3.place(x=450,y=210)
        self.controls_input_3.insert(0, "I/J/K/L/O")

        Label_4 = tk.Label(self.controls_window, text="Fourth player: ", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_4.place(x=305,y=240)
        self.controls_input_4=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_4.place(x=450,y=245)
        self.controls_input_4.insert(0, "Y/X/C/V/Q")

        Label_5 = tk.Label(self.controls_window, text="Fifth player :", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_5.place(x=305,y=275)
        self.controls_input_5=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_5.place(x=450,y=280)
        self.controls_input_5.insert(0, "B/N/M/SPACE/R")

        Label_6 = tk.Label(self.controls_window, text="Sixth player :", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_6.place(x=305,y=312)
        self.controls_input_6=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_6.place(x=450,y=315)
        self.controls_input_6.insert(0, "arrowLeft/arrowLeft/arrowDown/arrowRight/P")#key arrows

        Label_7 = tk.Label(self.controls_window, text="Active players :", font=tkfont.Font(family="Arial", size=16), fg="white", bg="#252423")
        Label_7.place(x=305,y=345)
        
        self.controls_input_7=tk.Entry(self.controls_window,bg="#7C7976",fg="Black",font=self.ButtonFont)
        self.controls_input_7.place(x=450,y=345)
        self.controls_input_7.insert(0, self.number_first)
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
        CloseButton = tk.Button(self.controls_window, text="Close", font=tkfont.Font(family="Impact", size=12), command=self.verif, bg="#7C7976")
        CloseButton.place(x=420,y=550)
WelcomeScreen()
