# **Regex to AFD: De Expresiones Regulares a Autómatas Finito Deterministas 🚀**

## 📌 Descripción del Proyecto
Este proyecto implementa el **método directo** para convertir **expresiones regulares** en **autómatas finitos deterministas (AFD)** utilizando el **algoritmo de metodo directo**. Posteriormente, el AFD generado es **minimizado** con el **algoritmo de Hopcroft**, reduciendo el número de estados sin alterar su funcionalidad.

---

## 🎯 ¿Qué Problema Resuelve?
Muchas aplicaciones requieren validar patrones de texto, como contraseñas, correos electrónicos o lenguajes de programación. Este proyecto permite convertir una **expresión regular** en un **AFD óptimo**, facilitando la validación eficiente de cadenas.

---

## 🏗️ Arquitectura del Proyecto
El proyecto está estructurado en distintos módulos clave:

### **1️⃣ Construcción del Árbol Sintáctico**
Se genera un árbol sintáctico a partir de la expresión regular en notación **postfija**.

- Se aplican reglas para calcular:
  - **Anulable** (si la subexpresión genera ε).
  - **Primera Posición** (posiciones iniciales de cada nodo).
  - **Última Posición** (posiciones finales de cada nodo).
  - **Siguiente Posición (Followpos)** (relaciones entre posiciones).

📂 **Archivo relevante:** `tree.py`

---

### **2️⃣ Construcción del AFD**
A partir del **Metodo Directo**, se construye un **AFD no minimizado**:

- Se definen los estados y las transiciones.
- Se establece el estado inicial y los estados finales.

📂 **Archivo relevante:** `direct_method.py`

---

### **3️⃣ Minimización del AFD**
Se usa el **algoritmo de minimización de Hopcroft** para reducir el número de estados sin alterar la funcionalidad.

📂 **Archivo relevante:** `minimization.py`

---

### **4️⃣ Evaluación de Cadenas**
Con el AFD generado, se pueden evaluar cadenas de entrada y determinar si son aceptadas o rechazadas.

📂 **Archivo relevante:** `simulation.py`

---

## 🚀 Ejemplo de Uso
### **🔹 Generar el AFD a partir de una expresión regular**
```python
from direct_method import direct_method

regex = "(a|b)+abc?"
afd = direct_method(regex=regex)  # Construcción del AFD
afd.imprimir()  # Imprimir la tabla de transiciones del AFD
```

### **🔹 Minimizar el AFD**
```python
from minimization import minAFD

afd_minimizado = minAFD(afd)
afd_minimizado.imprimir()
```

### **🔹 Evaluar una cadena**
```python
from simulation import evaluar_cadena

cadena = "aaaaabc"
if evaluar_cadena(afd_minimizado, cadena):
    print(f"La cadena '{cadena}' es aceptada.")
else:
    print(f"La cadena '{cadena}' NO es aceptada.")
```

---

## 🧪 Pruebas Unitarias
Se han implementado pruebas automáticas en `unittest` para validar la conversión y minimización del AFD.

📂 **Archivo relevante:** `tests/test_minAFD.py`

Ejecutar pruebas:
```bash
python -m unittest discover tests
```

---

## ⚙️ Instalación y Ejecución
### **🔹 Clonar el repositorio**
```bash
git clone https://github.com/tuusuario/regex_to_AFD.git
cd regex_to_AFD
```

### **🔹 Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **🔹 Ejecutar el programa**
```bash
python main.py
```

---

## 🛠️ Tecnologías Utilizadas
- **Python 3.9+**
- **Algoritmo de Metodo Directo**
- **Algoritmo de minimización de Hopcroft**
- **Unittest para pruebas automatizadas**

---
