# encoding:utf-8
from enum import Enum

class AgeCategories(Enum):
    CHILD = " < 10 ans"
    TEEN  = " >= 10 ans & < 20 ans"
    ADULT = " >= 20 ans"

class LevelCategories(Enum):
    EASY = "easy"
    INTERMEDIATE = "intermediate"
    HARD = "hard"