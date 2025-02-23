import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import expandir_operadores

class TestExpandirOperadores(unittest.TestCase):
    
    def test_expandir_operadores(self):
        test_cases = {
            "(a|b)+.a.b.c?" : "(a|b).(a|b)*.a.b.(c|E)", # Class sample
            "a+": "a.a*",
            "b?": "(b|E)",
            "(x|y)?": "((x|y)|E)",
            "z+": "z.z*",
            "(ab)+": "(ab).(ab)*",
            "c?d+": "(c|E).d.d*",
            "(a|b)+c?d": "(a|b).(a|b)*.(c|E).d", 
            "(p|q)+r?s+": "(p|q).(p|q)*.(r|E).s.s*",
            "(m+n)?o+": "((m.m*.n)|E).o.o*",
            "((x|y)+z)?w+": "(((x|y).(x|y)*.z)|E).w.w*"
            }
        
        for regex, expected in test_cases.items():
            self.assertEqual(expandir_operadores(regex), expected, f"Fallo en expandir_operadores con {regex}")

# Ejecutar las pruebas para `expandir_operadores`
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestExpandirOperadores))


