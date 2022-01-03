# encoding:utf-8
import tkinter as tk
from classes.Enums import AgeCategories
from tkinter import ttk, messagebox
from gui.GameWindow import GameWindow
from gui.ScoreboardWindow import ScoreboardWindow
from classes.Player import Player

class MainWindow(tk.Tk):

    def __init__(self, screenName=None, baseName=None, className="MainWindow", useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Spelling Game : Main Window")
        self.resizable(False, False)
        window_width = 400
        window_height = 300
        margin_x = int((self.winfo_screenwidth()/2) - (window_width/2))
        margin_y = int((self.winfo_screenheight()/2) - (window_height/2))
        self.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")
        
        font = ("Calibri Light", 12)
        
        tk.Label(self, text="Votre nom ", font=font).place(x=50, y=50)
        self.txt_nom = ttk.Entry(self, font=font )
        self.txt_nom.place(x=150, y=50)
        self.txt_nom.focus()
        
        tk.Label(self, text="Votre age", font=font).place(x=50, y=100)
        self.cb_age = ttk.Combobox(self, values=[age.value for age in AgeCategories], font=font)
        self.cb_age.place(x=150, y=100)
        self.cb_age.current(0)
        
        style = ttk.Style()
        style.configure("S.TButton", font = ("Calibri Light", 13, "bold"), foreground = "#117243")
        style.configure("R.TButton", font = ("Calibri Light", 13, "bold"), foreground = "#E20338")
        
        self.btn_commencez = ttk.Button(self, text="Commancez", style="S.TButton", command=self._commencez)
        self.btn_commencez.place(x=50, y=180)
        
        self.btn_tableau_scores = ttk.Button(self, text="Tableau de scores", style="R.TButton", command=self._scoreboard)
        self.btn_tableau_scores.place(x=190, y=180)
        

    def _commencez(self):
        name  = self.txt_nom.get().strip()
        level = self.cb_age.current()
        if name == "" or level == -1:
            messagebox.showwarning("Boîte de message", "Remplissez les informations demandées")
            return
        self.withdraw()
        GameWindow(self, player=Player(name=name, level=level))
        
    def _scoreboard(self):
        ScoreboardWindow(self)
        self.withdraw()
    
if __name__ == '__main__':
    MainWindow()
    tk.mainloop()