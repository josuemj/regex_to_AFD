def parsear_regex(regex: str) -> str:
    """
    Valida la expresión regular, elimina los operadores '+' y '?', y la convierte a una notación estándar
    agregando concatenaciones explícitas con ".".

    Parámetros:
    regex (str): Expresión regular ingresada.

    Retorna:
    str: Expresión regular en notación estándar sin los operadores '+' y '?'.
    """
  
    return regex

def aumentar_regex(regex: str) -> str:
    """
    Aumenta la expresión regular agregando el símbolo '#' al final.
    
    Parámetros:
        regex (str): Expresión regular en notación estándar.
    
    Retorna:
        str: Expresión regular aumentada (con '#' al final).
    """
    return regex+"#"



