# encoding:utf-8
from tkinter import messagebox
from _tkinter import TclError
import tkinter as tk
import time as tm
import random as rd

class MainWindow(tk.Toplevel):
    LEVELS = ("easy", "intermediate", "hard")
    def __init__(self, master=None, cnf={}, player=None):
        super().__init__(master, cnf)
        self.master = master
        self.player = player
        self.letter_buttons = []
        self.letter_labels = []
        self.hint_label = None
        self.score_label = None
        self.words = []
        self._load_words()
        self.word = ""
        self._select_random_word()
        self._basic_config()
        self._create_widgets(True)
     
    def _setup_new_word(self):
        if len(self.words) == 0 or self.word == "":
            return
        self.words.remove(self.word)
        self._select_random_word()
        self._delete_lettre_buttons()
        self._delete_guess_labels()
        self._create_widgets()
        
    def _basic_config(self):
        self.title(f"Spelling Game : {self.player.get_name()}")
        width = 400
        height = 300
        x = int((self.winfo_screenwidth()/2) - (width/2))
        y = int((self.winfo_screenheight()/2) - (height/2))
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.focus()
    
    def _create_widgets(self, init=False):
        if not init:
            self.btn_valider.destroy()
            self.score_label.config(text=f"Votre score est {self.player.get_score()} points", font=("Arial", 10))
            
        try :
            seconds = 5-self.player.get_level()
            
            self.hint_label = tk.Label(self, text=f"Votre mot est : {self.word} ({seconds} secondes)", font=("Arial", 13))
            self.hint_label.place(x=60, y=15)
            self.hint_label.after(seconds*1000, lambda : self.hint_label.destroy())
            for i in range(seconds):
                self.hint_label.config(text = f"Votre mot est '{self.word}' ({seconds-i} secondes)")
                self.update()
                tm.sleep(1)
            self._create_lettre_buttons()
            canvas = tk.Canvas(self, width=400, height=80)
            canvas.place(x=-2, y=232)
            self.btn_valider = tk.Button(self, text="Valider", font=("Arial", 12), command=lambda : self._check())
            self.btn_valider.place(x=len(self.word)*55, y=240)
            self._create_guess_labels()
            if init:
                self.score_label = tk.Label(self, text=f"Votre score est : {self.player.get_score()} points", font=("Arial", 10))
            self.score_label.place(x=220, y=275)
            self._animate_letter_buttons()
        except TclError:
            pass 
    
    def _load_words(self):
        if len(self.words) == 0 :
            self.words = eval(open(file=f"../files/levels/{MainWindow.LEVELS[self.player.get_level()]}.json").readline().upper().strip()) 
    
    def _select_random_word(self):
        if len(self.words) == 0 :
            messagebox.showinfo("Boîte de message", "Stage teminé")
            self._save_to_scoreboard()
            self.master.deiconify()
            self.destroy()
            return
        self.word = rd.choice(self.words)
     
    def _create_guess_labels(self):
        self.letter_labels.clear()
        for i in range(len(self.word)):
            try:
                lbl = tk.Label(self, font=("Arial", 12), bg="gray", fg="black", width=2, height=1)
                lbl.place(x=25+(i*50), y=250)
                self.letter_labels.append( lbl )
            except TclError:
                break
      
    def _delete_guess_labels(self):
        for lbl in self.letter_labels :
            lbl.destroy()
            
    def _create_lettre_buttons(self):
        letters = list( self.word )
        rd.shuffle(letters)
        self.letter_buttons.clear()
        X, Y = 70, 30
        for letter in letters :
            button = tk.Button(self, text=letter)
            button['command'] = lambda btn=button : self._on_click_letter_button(btn)
            button.place( x=X , y=Y)
            X += 30
            self.letter_buttons.append( button )
     
    def _delete_lettre_buttons(self):
        for btn in self.letter_buttons :
            btn.destroy()
          
    def _animate_letter_buttons(self):
        Y = 50
        while True:
            try:
                rd.choice(self.letter_buttons).place(y=Y)
                self.update()
                Y += 1
                tm.sleep((5-self.player.get_level())/150)
                if Y > 250 :
                    messagebox.showerror("Boîte de message", "Perdu")
                    break
            except TclError:
                break
        self._setup_new_word()
    
    def _on_click_letter_button(self, btn):
        for lbl in self.letter_labels:
            if lbl["text"] == "":
                lbl["text"] = btn["text"]
                btn["state"] = "disabled"
                break

    def _check(self):
        guess = []
        for letter in self.letter_labels:
            guess.append(letter["text"])
        if "".join(guess) == self.word:
            self.player.increment_score()
            messagebox.showinfo("Boîte de message", "Bien Joué")
            self._setup_new_word()
        else:
            messagebox.showwarning("Boîte de message", "Reéssayer")

    def _save_to_scoreboard(self):
        file = open(file=f"../files/scoreboards/{MainWindow.LEVELS[self.player.get_level()]}.json")
        scoreboard = eval(file.readline().strip())
        scoreboard.append(dict(self.player))
        file = open(file=f"../files/scoreboards/{MainWindow.LEVELS[self.player.get_level()]}.json", mode="w")
        file.write( str(scoreboard) )
        file.close()