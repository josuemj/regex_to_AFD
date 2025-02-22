from typing import Set, Dict, Tuple

class AFD:
    """
    Clase que representa un Autómata Finito Determinista (AFD).

    Atributos:
        Q (Set[str]): Conjunto de estados.
        A (Set[str]): Conjunto de símbolos (alfabeto).
        T (Dict[Tuple[str, str], str]): Función de transición, mapea (estado actual, símbolo) a nuevo estado.
        q0 (str): Estado inicial.
        F (Set[str]): Conjunto de estados de aceptación.
    """
    
    def __init__(self, 
                 Q: Set[str], 
                 A: Set[str], 
                 T: Dict[Tuple[str, str], str], 
                 q0: str, 
                 F: Set[str]) -> None:
        """
        Inicializa la instancia del AFD con los parámetros dados.

        Parámetros:
            Q (Set[str]): Conjunto de estados.
            A (Set[str]): Conjunto de símbolos (alfabeto).
            T (Dict[Tuple[str, str], str]): Función de transición.
            q0 (str): Estado inicial.
            F (Set[str]): Conjunto de estados de aceptación.
        """
        self.Q: Set[str] = Q
        self.A: Set[str] = A
        self.T: Dict[Tuple[str, str], str] = T
        self.q0: str = q0
        self.F: Set[str] = F

    def __repr__(self) -> str:
        return (f"AFD(Q={self.Q}, A={self.A}, T={self.T}, "
                f"q0='{self.q0}', F={self.F})")

