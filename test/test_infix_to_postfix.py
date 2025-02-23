import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.shunting_yard import shunting_yard
from src.syntax_tree import convertir_a_posfijo
class TestShuntingYard(unittest.TestCase):
    
    def test_shunting_yard(self):
        test_cases = {
            "a.b": "ab.",
            "a|b": "ab|",
            "(a.b)*": "ab.*",
            "a.b.c": "ab.c.",
            "a.(b|c).d": "abc|.d.",
            "(x|y)*.z": "xy|*z.",
            "a.(b.c|d)*": "abc.d|*.",
            "(a|b).(a|b)*.a.b.(c|E)" : "ab|ab|*.a.b.cE|." #class sample
        }
        
        for regex, expected in test_cases.items():
            self.assertEqual(shunting_yard(regex), expected, f"Fallo en shunting_yard con {regex}")
            self.assertEqual(convertir_a_posfijo(regex), expected, f"Fallo en shunting_yard con {regex}") #misma llamada a 

# Ejecutar las pruebas para `shunting_yard`
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestShuntingYard))
