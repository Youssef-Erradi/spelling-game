# encoding:utf-8
import gui.Constences as CONSTS
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui.GameWindow import GameWindow
from classes.Player import Player

class MainWindow():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Splash screen")
        self.root.resizable(False, False)
        window_width = 400
        window_height = 300
        margin_x = int((self.root.winfo_screenwidth()/2) - (window_width/2))
        margin_y = int((self.root.winfo_screenheight()/2) - (window_height/2))
        self.root.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")
        
        tk.Label(self.root, text="Votre nom").place(x=50, y=50)
        self.txt_nom = tk.Entry(self.root)
        self.txt_nom.place(x=150, y=50)
        self.txt_nom.focus()
        
        tk.Label(self.root, text="Votre age").place(x=50, y=100)
        self.cb_age = ttk.Combobox(self.root, values=CONSTS.AGE_CATEGORIES)
        self.cb_age.place(x=150, y=100)
        self.cb_age.current(0)
        
        self.btn_commencez = tk.Button(self.root, text="Commancez", font=("Calibri Light",13), command=self._commencez)
        self.btn_commencez.place(x=150, y=180)
        
        tk.mainloop()

    def _commencez(self):
        name  = self.txt_nom.get().strip()
        level = self.cb_age.current()
        if name == "" or level == -1:
            messagebox.showwarning("Boîte de message", "Entrez les informations demandées")
            return
        self.root.withdraw()
        GameWindow(self.root, player=Player(name=name, level=level))
