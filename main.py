import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.parser import parsear_regex

from direct_method import direct_method
from src.simulation import simulate_afd

# E = epsilon

regex = "(a|b)+abc?"

afd = direct_method(regex=regex) # afd()

cadena = "aabc"

# pertenece = simulate_afd(afd=afd) # bool