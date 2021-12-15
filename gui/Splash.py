# encoding:utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui.MainWindow import MainWindow
from classes.Player import Player

age_categories = (" < 10 ans"," >= 10 ans & < 18 ans"," >= 18 ans")

def commencez():
    name  = txt_nom.get().strip()
    level = cb_age.current()
    if name == "" or level == -1:
        messagebox.showwarning("Boîte de message", "Entrez les informations demandées")
        return
    root.withdraw()
    MainWindow(root, player=Player(name=name, level=level))
    
root = tk.Tk()
root.title("Splash screen")
root.resizable(False, False)
window_width = 400
window_height = 300
margin_x = int((root.winfo_screenwidth()/2) - (window_width/2))
margin_y = int((root.winfo_screenheight()/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")

tk.Label(root, text="Votre nom").place(x=50, y=50)
txt_nom = tk.Entry(root)
txt_nom.place(x=150, y=50)
txt_nom.focus()

tk.Label(root, text="Votre age").place(x=50, y=100)
cb_age = ttk.Combobox(root, values=age_categories)
cb_age.place(x=150, y=100)
cb_age.current(0)

btn_commencez = tk.Button(root, text="Commancez", font=("Calibri Light",13), command=commencez)
btn_commencez.place(x=150, y=180)

tk.mainloop()