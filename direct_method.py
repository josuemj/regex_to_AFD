from typing import Dict, Any
from src.model.afd import AFD
from src.parser import parsear_regex, aumentar_regex #1, 2
from src.syntax_tree import construir_arbol, calcular_anulable, calcular_primera_pos
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
    
    # 1 agregar concatenación y quitar los operadores que no reconoce el método directo 
    regex_parse = parsear_regex(regex=regex)
    
    # 2 aumentar la expresion con #
    regex_aumentada = aumentar_regex(regex=regex_parse)
    
    # 3 arbol sintactico
    arbol = construir_arbol(regex=regex_aumentada)
    
    # 4 Calcular anulable

    arbol = calcular_anulable(arbol)

    # 5 Calcular Funcion Primera Posicion
    arrbol = calcular_primera_pos(arbol)