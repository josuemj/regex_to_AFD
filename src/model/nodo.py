from typing import Optional, Set


class Nodo:
    """
    Representa un nodo en el árbol sintáctico de la expresión regular.
    
    Atributos:
        valor (str): El símbolo o operador del nodo.
        izquierdo (Optional[Nodo]): Hijo izquierdo (puede ser None).
        derecho (Optional[Nodo]): Hijo derecho (puede ser None).
        anulable (bool): Indica si la subexpresión representada por este nodo puede generar ε.
        primera_pos (Set[int]): Conjunto de posiciones posibles que pueden aparecer primero.
        ultima_pos (Set[int]): Conjunto de posiciones posibles que pueden aparecer al final.
    """
    def __init__(self, valor: str, 
                 izquierdo: Optional['Nodo'] = None, 
                 derecho: Optional['Nodo'] = None) -> None:
        self.valor: str = valor
        self.izquierdo: Optional[Nodo] = izquierdo
        self.derecho: Optional[Nodo] = derecho
        self.anulable: bool = False
        self.primera_pos: Set[int] = set()
        self.ultima_pos: Set[int] = set()