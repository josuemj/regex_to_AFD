import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.parser import parsear_regex
from direct_method import direct_method
from src.simulation import evaluar_cadena
from src.build_afd import min_afd
# E = epsilon

regex = "(a|b)+abc?"
afd = direct_method(regex=regex) # afd()

# afd_min = min_afd(afd=afd) 

cadena = "aaaaabc"

aceptada = evaluar_cadena(afd, cadena)
if aceptada:
    print(f"La cadena '{cadena}' es aceptada por el AFD.")
else:
    print(f"La cadena '{cadena}' NO es aceptada por el AFD.")
