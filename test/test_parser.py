import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import agregar_concatenacion

class TestAgregarConcatenacion(unittest.TestCase):
    
    def test_agregar_concatenacion(self):
        test_cases = {
            "ab": "a.b",                  
            "a(b|c)d": "a.(b|c).d",        
            "(a|b)*c": "(a|b)*.c",         
            "a?b+": "a?.b+",               
            "(ab)c": "(a.b).c",            
            "a(bc)d": "a.(b.c).d",         
            "a|b*cd": "a|b*.c.d",          
            "a(b|c)*d": "a.(b|c)*.d",      
            "x+y?z": "x+.y?.z",            
            "(a|b)+(c|d)": "(a|b)+.(c|d)"  
        }
        
        for regex, expected in test_cases.items():
            self.assertEqual(agregar_concatenacion(regex), expected, f"Fallo en agregar_concatenacion con {regex}")

# Ejecutar las pruebas para `agregar_concatenacion`
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestAgregarConcatenacion))
