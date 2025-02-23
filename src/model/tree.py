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
    
    def calcular_anulable(self, nodo: Optional[Nodo]) -> bool:
        """
        Calcula si un nodo es anulable (si acepta la cadena vacía) y lo almacena en su atributo `anulable`.
        Devuelve `True` si el nodo es anulable, `False` en caso contrario.
        """

        if nodo is None:
            return False

        # Si es un nodo hoja
        if nodo.izquierdo is None and nodo.derecho is None:
            nodo.anulable = nodo.valor == "E"  # Un nodo hoja solo es anulable si es 'E' (ε)
            print(f"Nodo: {nodo.valor}, Anulable: {nodo.anulable}") 
            return nodo.anulable

        # Primero calcular anulabilidad en los hijos recursivamente
        izq_anulable = self.calcular_anulable(nodo.izquierdo) if nodo.izquierdo else False
        der_anulable = self.calcular_anulable(nodo.derecho) if nodo.derecho else False

        # Aplicar reglas de operadores
        if nodo.valor == "|":  # Unión: anulable si al menos un hijo lo es
            nodo.anulable = izq_anulable or der_anulable
        elif nodo.valor == ".":  # Concatenación: anulable si ambos lo son
            nodo.anulable = izq_anulable and der_anulable
        elif nodo.valor == "*":  # Kleene: siempre anulable
            nodo.anulable = True

        # Mostrar información del nodo después de calcular su anulabilidad
        print(f"Nodo: {nodo.valor}, Anulable: {nodo.anulable}") 

        return nodo.anulable

    def calcular_primeraPosicion(self, nodo:Optional[Nodo]) -> Set[int]:
        """
        Calcula la primera posición de cada nodo en el árbol sintáctico.
        """

        if nodo is None:
            return set()
        
        #Si es hoja final, su primera posicion es su posicion
        if nodo.izquierdo is None and nodo.derecho is None:
            nodo.primera_pos = {nodo.posicion} if nodo.posicion is not None else set()
            print(f"Nodo: {nodo.valor}, PrimeraPosición: {nodo.primera_pos}")
            return nodo.primera_pos

        # Si es un operador, calcular recursivamente en sus hijos
        izq_primera = self.calcular_primeraPosicion(nodo.izquierdo) if nodo.izquierdo else set()
        der_primera = self.calcular_primeraPosicion(nodo.derecho) if nodo.derecho else set()

        if nodo.valor == "|":  # Unión: unión de ambos hijos
            nodo.primera_pos = izq_primera | der_primera
        elif nodo.valor == ".":  # Concatenación
            if nodo.izquierdo.anulable:
                nodo.primera_pos = izq_primera | der_primera
            else:
                nodo.primera_pos = izq_primera
        elif nodo.valor == "*":  # Kleene: primeraposición es igual a la del hijo
            nodo.primera_pos = izq_primera

        print(f"Nodo: {nodo.valor}, PrimeraPosición: {nodo.primera_pos}")
        return nodo.primera_pos

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