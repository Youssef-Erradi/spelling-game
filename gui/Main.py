import tkinter as tk
import time as tm
import random as rd
from _tkinter import TclError

buttons, guesses, words = [], [], []
word = ""
X, Y = 30, 50
level = 0

def action(btn):
    for lbl in guesses:
        if lbl["text"] == "":
            lbl["text"] = btn["text"]
            btn["state"] = "disabled"
            break

def check():
    guess = []
    for letter in guesses:
        guess.append(letter["text"])
    if "".join(guess) == word:
        print("Well done !")
        # window.withdraw()
        # root.deiconify()
        create_lettre_buttons()
        animate_letter_buttons()
    else:
        print("Not quite :)")

def create_window(master, lvl=0, nom=""):
    global window
    global root
    root = master
    window = tk.Toplevel(root)
    window.title(f"Spelling Game : {nom}")
    window_width = 400
    window_height = 300
    margin_x = int((window.winfo_screenwidth()/2) - (window_width/2))
    margin_y = int((window.winfo_screenheight()/2) - (window_height/2))
    window.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")
    if lvl > 0:
        level = lvl
        print(lvl,nom)
    create_lettre_buttons()
    btn_valider = tk.Button(window, text="Valider", font=("Arial", 12), command=lambda : check())
    btn_valider.place(x=len(word)*55, y=240)
    
    animate_letter_buttons()

def load_words(level=0):
    global words
    levels = ("easy", "intermediate", "hard")
    if len(words) == 0 :
        words = eval( open(file=f"../files/levels/{levels[level]}.json", mode="r").readline().upper().strip() )

def select_random_word():
    global word
    if len(words) == 0:
        load_words()
    if word == "":
        word = rd.choice(words)
    else:
        words.remove(word)
        word=rd.choice(words)

def create_lettre_buttons():
    global X, Y
    select_random_word()
    letters = list( word )
    rd.shuffle(letters)
    buttons.clear()
    X, Y = 30, 50
    for letter in letters :
        button = tk.Button(window, text=letter)
        button['command'] = lambda btn=button : action(btn)
        button.place( x=X , y=Y)
        X += 30
        buttons.append( button )
    create_guess_labels()
    
def create_guess_labels():
    for i in range(len(word)):
        try:
            lbl = tk.Label(window, font=("Arial", 12), bg="gray", fg="black", width=2, height=1)
            lbl.place(x=25+(i*50), y=250)
            guesses.append( lbl )
        except TclError:
            break
            
def animate_letter_buttons():
    global X, Y
    while True:
        try:
            rd.choice(buttons).place(y=Y)
            window.update()
            Y += 1
            tm.sleep(0.1)
        except TclError:
            break