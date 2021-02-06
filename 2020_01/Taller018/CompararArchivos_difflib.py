# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:35:39 2020

@author: Ander
"""

import difflib

print("Demo 18: Comparación de Archivos con difflib")

archivoOrigen = input("Ingresa Archivo Original: ")
archivoComparar = input("Ingresa Archivo Comparar: ")
lineaOrigen = open(archivoOrigen,"r").readlines()
lineaComparar = open(archivoComparar,"r").readlines()


html = difflib.HtmlDiff()
rpta = html.make_file(lineaOrigen,lineaComparar,archivoOrigen,archivoComparar)
open("Diferencias.html","w").write(rpta)
print("Archivo html fue creado")

