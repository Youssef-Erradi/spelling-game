import tkinter as tk
from classes.Enums import LevelCategories

class ScoreboardWindow(tk.Toplevel):
    
    def __init__(self, master=None, cnf={}):
        super().__init__(master, cnf)
        self.__scoreboard = []
        self._basic_config()
        self._load_data()
        self._show()
        
    def _basic_config(self):
        self.title("Spelling Game : Scoreboard Window")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self._on_close)
    
    def _on_close(self):
        self.master.deiconify()
        self.destroy()
    
    def _load_data(self, sort=True):
        for level in LevelCategories:
            with open(file=f"../files/scoreboards/{level.value}.json") as file:
                for player in eval( file.readline().strip() ):
                    self.__scoreboard.append(player)
        if(sort):
            self.__scoreboard.sort(key=lambda player:(player["score"],player["level"]), reverse=True)
            
    def _show(self):
        font = ("Calibri Light", 12)
        tk.Label(self,text="Nom", font=("Calibri Light", 12, "bold")).grid(row=0, column=0, sticky=tk.NSEW)
        tk.Label(self,text="Score", font=("Calibri Light", 12, "bold")).grid(row=0, column=1, sticky=tk.NSEW)
        tk.Label(self,text="Niveau", font=("Calibri Light", 12, "bold")).grid(row=0, column=2, sticky=tk.NSEW)
        for i,player in enumerate(self.__scoreboard) :
            tk.Label(self,text=player["name"], font=font).grid(row=i+1, column=0, sticky=tk.NSEW)
            tk.Label(self,text=player["score"], font=font).grid(row=i+1, column=1, sticky=tk.NSEW)
            tk.Label(self,text=list(LevelCategories)[player["level"]].value, font=font).grid(row=i+1, column=2, sticky=tk.NSEW)