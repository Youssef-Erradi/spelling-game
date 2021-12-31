# encoding:utf-8
from enum import Enum

class AgeCategories(Enum):
    CHILD = " < 10 ans"
    TEEN  = " >= 10 ans & < 18 ans"
    ADULT = " >= 18 ans"

class LevelCategories(Enum):
    EASY = "easy"
    INTERMEDIATE = "intermediate"
    HARD = "hard"