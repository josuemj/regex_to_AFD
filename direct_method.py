from typing import Dict, Any
from src.model.afd import AFD
def direct_method(regex: str) -> AFD:
    """
    Aplica el método directo (Followpos Algorithm) para convertir una expresión regular a un AFD.

    Parámetros:
        regex (str): Expresión regular de entrada.

    Retorna:
        AFD: El AFD resultante representado como un diccionario que incluye:
            - "Q": Conjunto de estados.
            - "A": Alfabeto.
            - "T": Función de transición.
            - "q0": Estado inicial.
            - "F": Conjunto de estados de aceptación.
    """