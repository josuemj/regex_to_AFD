import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from direct_method import direct_method


import unittest
from direct_method import direct_method
from src.simulation import evaluar_cadena

class TestMetodoDirecto(unittest.TestCase):
    
    def setUp(self):
        self.regex = "(a|b)+abc?"
        self.afd = direct_method(self.regex)

    def test_cadenas_aceptadas(self):
        aceptadas = [
            "aaaaabc",
            "abababc",
            "ababc",
            "aabc"
        ]
        for cadena in aceptadas:
            with self.subTest(cadena=cadena):
                self.assertTrue(evaluar_cadena(self.afd, cadena), f"La cadena '{cadena}' debería ser aceptada.")

    def test_cadenas_rechazadas(self):
        rechazadas = [
            "",
            "a",
            "ab",
            "ba",
            "babcab",
            "cba"
        ]
        for cadena in rechazadas:
            with self.subTest(cadena=cadena):
                self.assertFalse(evaluar_cadena(self.afd, cadena), f"La cadena '{cadena}' NO debería ser aceptada.")
                
unittest.main()
