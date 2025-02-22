from typing import Dict, Any, Set
from model.afd import AFD

def construir_afd(tabla_transicion: Dict[Any, Any], primera_pos: Set[Any]) -> AFD:
    """
    Construye el AFD a partir de la tabla de transición y la primera posición del árbol sintáctico.

    Parámetros:
        tabla_transicion (Dict[Any, Any]): Tabla de transición que mapea (estado, símbolo) a nuevo estado.
        primera_pos (Set[Any]): Conjunto de posiciones de la raíz del árbol sintáctico, usado para definir el estado inicial.

    Retorna: AFD
    """
    pass
