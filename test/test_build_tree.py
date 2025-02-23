import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.model.tree import Tree

expresion_postfija = "ab|ab|*.a.b.cE|."
arbol = Tree(expresion_postfija)

