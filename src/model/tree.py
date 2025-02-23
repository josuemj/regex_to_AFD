from typing import Optional, Set

from src.model.nodo import Nodo
from src.model.stack import Stack

from typing import Optional
from src.model.nodo import Nodo
from src.model.stack import Stack

class Tree:
    """
    Representa un árbol sintáctico construido a partir de una expresión regular en notación postfija.
    """
    def __init__(self, expresion_postfija: str):
        self.expresion_postfija = expresion_postfija
        self.raiz: Optional[Nodo] = self.construir_arbol()

    def construir_arbol(self) -> Optional[Nodo]:
        """
        Construye el árbol sintáctico a partir de la expresión regular en notación postfija.
        Utiliza una pila basada en la clase Stack para manejar los operandos y operadores.
        """
        pila = Stack()
        posicion = 1  # Contador para asignar posiciones a los nodos hoja

        print("\n====== Construcción del Árbol Sintáctico ======\n")

        for caracter in self.expresion_postfija:
            print(f"🔹 Procesando: {caracter}")
            print(f"  📍 Pila antes de procesar: {[n.valor for n in pila.items]}")

            # ✅ Tratar '#' como un operando, igual que 'a', 'b', 'E', etc.
            if caracter.isalnum() or caracter in {'E', '#'}:  # Si es un operando (letra, 'E' para ε, '#' como marcador)
                posicion_nodo = None if caracter == 'E' else posicion
                nodo = Nodo(valor=caracter, posicion=posicion_nodo )
                pila.push(nodo)
                if caracter != 'E':  # Solo incrementar la posición si NO es epsilon
                    posicion += 1
                print(f"  ✅ Se agregó nodo hoja: {nodo.valor} (Pos: {nodo.posicion})")

            elif caracter in {'|', '.', '*'}:  # Si es un operador
                if caracter == '*':  # Operador unario (Cerradura de Kleene)
                    if pila.is_empty():  # Evitar errores de pila vacía
                        raise ValueError("Expresión postfija mal formada: falta operando para '*'")
                    hijo = pila.pop()
                    nodo = Nodo(valor=caracter, izquierdo=hijo)
                    print(f"  🔄 Se creó nodo * con hijo {hijo.valor}")

                else:  # Operador binario ('|' o '.')
                    if pila.is_empty():
                        raise ValueError(f"Expresión postfija mal formada: falta operandos para '{caracter}'")
                    derecho = pila.pop()
                    if pila.is_empty():
                        raise ValueError(f"Expresión postfija mal formada: falta operandos para '{caracter}'")
                    izquierdo = pila.pop()
                    nodo = Nodo(valor=caracter, izquierdo=izquierdo, derecho=derecho)
                    print(f"  🔄 Se creó nodo {caracter} con hijos {izquierdo.valor}, {derecho.valor}")

                pila.push(nodo)

            print(f"  📍 Pila después de procesar: {[n.valor for n in pila.items]}")
            print("-" * 50)

        if pila.is_empty() or len(pila.items) != 1:
            raise ValueError("Expresión postfija mal formada: faltan operadores")

        print("\n✅ Árbol construido correctamente\n")
        return pila.pop()  # Raíz del árbol sintáctico
