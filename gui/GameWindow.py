# encoding:utf-8
from tkinter import messagebox,TclError,ttk
from classes.Enums import LevelCategories
import tkinter as tk
import time as tm
import random as rd

class GameWindow(tk.Toplevel):
    
    def __init__(self, master, player, cnf={}):
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
     
    def _basic_config(self):
        self.title(f"Spelling Game : {self.player.get_name()}")
        width = 450+(self.player.get_level()*70)
        height = 300
        x = int((self.winfo_screenwidth()/2) - (width/2))
        y = int((self.winfo_screenheight()/2) - (height/2))
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.protocol("WM_DELETE_WINDOW", self._on_close)
    
    def _on_close(self):
        self.wm_withdraw()
        messagebox.showerror("Boîte de message", "Partie Annulée")
        self.master.destroy()
    
    def _setup_new_word(self):
        if len(self.words) == 0 or self.word == "":
            return
        self.words.remove(self.word)
        self._select_random_word()
        self._delete_lettre_buttons()
        self._delete_guess_labels()
        self._create_widgets()      
    
    def _create_widgets(self, init=False):
        try :
            if not init:
                self.btn_valider.destroy()
                self.btn_effacer.destroy()
                self.score_label["text"] = f"Votre score est : {self.player.get_score()} points"  
            seconds = 5-self.player.get_level()
            self.hint_label = tk.Label(self, text=f"Votre mot est : {self.word} ({seconds} secondes)", font=("Calibri Light", 15))
            self.hint_label.place(x=80, y=15)
            self.hint_label.after(seconds*1000, lambda : self.hint_label.destroy())
            for i in range(seconds):
                self.hint_label.config(text = f"Votre mot est '{self.word}' ({seconds-i} secondes)")
                self.update()
                tm.sleep(1)
            self._create_lettre_buttons()
            canvas = tk.Canvas(self, width=400, height=80)
            canvas.place(x=-2, y=232)
            self.btn_valider = ttk.Button(self, text="Valider", style="S.TButton", command=lambda : self._check())
            self.btn_valider.place(x=len(self.word)*55, y=250)
            self.btn_effacer = ttk.Button(self, text="Réinitialiser", style="R.TButton", command=lambda : self._reset())
            self.btn_effacer.place(x=len(self.word)*55+120, y=250)
            self._create_guess_labels()
            self._create_score_label()
            self._animate_letter_buttons()
        except TclError:
            exit(0) 
    
    def _create_score_label(self):
        self.score_label = tk.Label(self, text=f"Votre score est : {self.player.get_score()} points", font=("Calibri Light", 10))
        self.score_label.place(x=220+(self.player.get_level()*50), y=280)
    
    def _load_words(self):
        if len(self.words) == 0 :
            with open(file=f"../files/levels/{list(LevelCategories)[self.player.get_level()].value}.json") as file :
                self.words = eval( file.readline().upper().strip()) 
    
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
                lbl = tk.Label(self, font=("Calibri Light", 12, "bold"), bg="#D1D3D4", fg="black", width=2, height=1)
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
        X, Y = 70, 20
        for letter in letters :
            button = tk.Button(self, text=letter, font=("Calibri Light", 12))
            button['command'] = lambda btn=button : self._on_click_letter_button(btn)
            button.place( x=X , y=Y)
            X += 50
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
                tm.sleep((5-self.player.get_level())/100)
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

    def _reset(self):
        for btn in self.letter_buttons:
            btn["state"] = "normal"
        for lbl in self.letter_labels:
            lbl["text"] = ""

    def _save_to_scoreboard(self):
        file = open(file=f"../files/scoreboards/{list(LevelCategories)[self.player.get_level()].value}.json")
        scoreboard = eval(file.readline().strip())
        scoreboard.append(dict(self.player))
        with open(file=f"../files/scoreboards/{list(LevelCategories)[self.player.get_level()].value}.json", mode="w") as file :
            file.write( str(scoreboard).replace("'", "\"") )
