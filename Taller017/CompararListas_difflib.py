# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:21:20 2020

@author: Ander
"""

import difflib

print("Demo 17: Comparación de listas con difflib")
lista1 =["Ander","Jesus","Mili","Juan Carlos", "Arturo"]
lista2 = ["Ander","Marco","Edward","Arturo"]
diferencia = difflib.context_diff(lista1, lista2)
for fila in diferencia:
    print(fila)
#print(type(diferencia))

