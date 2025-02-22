def parsear_regex(regex: str) -> str:
    """Agrega concatenaciones y expande operadores `?` y `+`."""
    regex_concatenada = agregar_concatenacion(regex)
    regex_expandida = expandir_operadores(regex_concatenada)
    return regex_expandida

# Reescribir la función `agregar_concatenacion` asegurando que funcione correctamente con pruebas específicas

def agregar_concatenacion(regex: str) -> str:
    """Añade explícitamente el operador de concatenación '.' a la expresión regular sin insertar dentro de grupos."""
    resultado = ""
    operadores = {'|', '*', '?', '+'}

    for i in range(len(regex)):
        actual = regex[i]
        resultado += actual

        if i + 1 < len(regex):
            siguiente = regex[i + 1]

            # Si actual es un símbolo o cierre y siguiente es símbolo o apertura, añadir concatenación
            if (actual not in operadores and actual != '(') and \
               (siguiente not in operadores and siguiente != ')' and siguiente not in {'|', '*', '?', '+'}):
                resultado += '.'

            # Si actual es cierre de paréntesis, '*', '+', '?' y siguiente es un símbolo o apertura de paréntesis, añadir concatenación
            if (actual in {'*', '?', '+', ')'} and (siguiente not in operadores and siguiente != ')' and siguiente != '|')):
                resultado += '.'

    # Evitar concatenaciones duplicadas
    while ".." in resultado:
        resultado = resultado.replace("..", ".")

    return resultado


def expandir_operadores(regex: str) -> str:
    """Sustituye los operadores `+` y `?` por sus equivalentes en `*` y `|ε`."""
    resultado = ""
    i = 0
    while i < len(regex):
        if regex[i] == '+':  # A+ -> A·A*
            anterior = resultado[-1]
            if anterior != ')':  # Si es un solo carácter
                resultado += '·' + anterior + '*'
            else:  # Si es una subexpresión (cerrada con ')')
                # Buscar el inicio de la subexpresión
                parentesis = 1
                j = len(resultado) - 2
                while j >= 0 and parentesis > 0:
                    if resultado[j] == ')':
                        parentesis += 1
                    elif resultado[j] == '(':
                        parentesis -= 1
                    j -= 1
                subexpresion = resultado[j+1:]  # Extraer subexpresión
                resultado += '·' + subexpresion + '*'  # A+ -> A·A*
        
        elif regex[i] == '?':  # A? -> A|ε
            anterior = resultado[-1]
            if anterior != ')':  # Si es un solo carácter
                resultado = resultado[:-1] + '(' + anterior + '|ε)'
            else:  # Si es una subexpresión
                # Buscar el inicio de la subexpresión
                parentesis = 1
                j = len(resultado) - 2
                while j >= 0 and parentesis > 0:
                    if resultado[j] == ')':
                        parentesis += 1
                    elif resultado[j] == '(':
                        parentesis -= 1
                    j -= 1
                subexpresion = resultado[j+1:]  # Extraer subexpresión
                resultado = resultado[:j+1] + '(' + subexpresion + '|ε)'
        
        else:
            resultado += regex[i]
        
        i += 1

    return resultado

def aumentar_regex(regex: str) -> str:
    """
    Aumenta la expresión regular agregando el símbolo '#' al final.
    
    Parámetros:
        regex (str): Expresión regular en notación estándar.
    
    Retorna:
        str: Expresión regular aumentada (con '#' al final).
    """
    return regex+"#"



