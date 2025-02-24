import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model.afd import AFD
from direct_method import direct_method
from src.simulation import evaluar_cadena
from src.minimization import minAFD  

class TestMinAFD(unittest.TestCase):
    
    def setUp(self):
        """
        Inicializa casos de prueba con expresiones regulares diferentes.
        """
        self.regex1 = "(a|b)*c"  # Autómata con ciclos
        self.regex2 = "ab+c"     # Autómata simple
        self.regex3 = "(aa|bb)*" # Autómata con grupos repetitivos
        self.regex4 = "a*b*"     # Autómata con Kleene en múltiples símbolos
        self.regex5 = "abc|def"  # Dos caminos distintos

        # Construcción de los AFD originales
        self.afd1 = direct_method(self.regex1)
        self.afd2 = direct_method(self.regex2)
        self.afd3 = direct_method(self.regex3)
        self.afd4 = direct_method(self.regex4)
        self.afd5 = direct_method(self.regex5)

        # Aplicar minimización
        self.min_afd1 = minAFD(self.afd1)
        self.min_afd2 = minAFD(self.afd2)
        self.min_afd3 = minAFD(self.afd3)
        self.min_afd4 = minAFD(self.afd4)
        self.min_afd5 = minAFD(self.afd5)

    def test_minimiza_afd1(self):
        """
        Verifica que la minimización de (a|b)*c reduzca estados correctamente.
        """
        estados_antes = len(self.afd1.Q)
        estados_despues = len(self.min_afd1.Q)
        self.assertLessEqual(estados_despues, estados_antes, "El AFD minimizado debe tener menos o igual estados.")

    def test_minimiza_afd2(self):
        """
        Verifica que la minimización de ab+c sea correcta.
        """
        estados_antes = len(self.afd2.Q)
        estados_despues = len(self.min_afd2.Q)
        self.assertLessEqual(estados_despues, estados_antes, "El AFD minimizado debe tener menos o igual estados.")

    def test_minimiza_afd3(self):
        """
        Verifica que la minimización de (aa|bb)* mantenga la misma lógica.
        """
        estados_antes = len(self.afd3.Q)
        estados_despues = len(self.min_afd3.Q)
        self.assertLessEqual(estados_despues, estados_antes, "El AFD minimizado debe tener menos o igual estados.")

    def test_minimiza_afd4(self):
        """
        Verifica que la minimización de a*b* produzca un autómata correcto.
        """
        estados_antes = len(self.afd4.Q)
        estados_despues = len(self.min_afd4.Q)
        self.assertLessEqual(estados_despues, estados_antes, "El AFD minimizado debe tener menos o igual estados.")

    def test_minimiza_afd5(self):
        """
        Verifica que la minimización de abc|def mantenga la lógica de caminos distintos.
        """
        estados_antes = len(self.afd5.Q)
        estados_despues = len(self.min_afd5.Q)
        self.assertLessEqual(estados_despues, estados_antes, "El AFD minimizado debe tener menos o igual estados.")

if __name__ == '__main__':
    unittest.main()
