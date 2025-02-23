# src/syntax_tree.py
from typing import Optional, Set
from src.model.nodo import Nodo
from src.utils.shunting_yard import shunting_yard
from model.tree import Tree

def convertir_a_posfijo(regex: str) -> str:
    """
    Convierte una expresión regular en notación infija a notación posfija utilizando el algoritmo Shunting Yard.
    
    Parámetros:
        regex (str): Expresión regular en notación infija.
    
    Retorna:
        str: Expresión regular en notación posfija.
    """
    postfix = shunting_yard(regex=regex)
    print('postfix -> '+postfix)
    return postfix

def construir_arbol(regex: str) -> Tree:
    """
    Construye el árbol sintáctico a partir de una expresión regualar.
    
    Parámetros:
        posfijo (str): Expresión regular en notación posfija.
    
    Retorna:
        Tree: árbol sintáctico construido.
    """
    postfijo = convertir_a_posfijo(regex)
    return Tree(expresion_postfija=postfijo)
     

def calcular_anulable(raiz: Nodo) -> None:
    """
    Calcula la propiedad anulable para cada nodo del árbol sintáctico.
    
    Parámetros:
        raiz (Nodo): Raíz del árbol sintáctico.
    """
    pass

def calcular_primera_pos(raiz: Nodo) -> None:
    """
    Calcula la primera posición para cada nodo del árbol sintáctico.
    
    Parámetros:
        raiz (Nodo): Raíz del árbol sintáctico.
    """
    pass

def calcular_ultima_pos(raiz: Nodo) -> None:
    """
    Calcula la última posición para cada nodo del árbol sintáctico.
    
    Parámetros:
        raiz (Nodo): Raíz del árbol sintáctico.
    """
    pass

def calcular_siguiente_pos(raiz: Nodo) -> None:
    """
    Calcula la siguiente posición para cada nodo del árbol sintáctico basado en la función siguiente.
    
    Parámetros:
        raiz (Nodo): Raíz del árbol sintáctico.
    """
    pass
