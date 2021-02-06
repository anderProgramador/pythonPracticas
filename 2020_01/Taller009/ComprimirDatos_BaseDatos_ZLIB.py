# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:11:59 2020

@author: Ander
"""

from modProducto import Producto
import zlib

print("Demo 09: Compresión de Datos usando la librería zlib")
oProducto = Producto("Config.ini")
data = oProducto.ListarCsv()
print("Data sin Comprimir")
print(data)
print("Tamaño de data sin Comprimir: ", len(data))
input("Pulsa enter para continuar")

bytesSinComprimir = data.encode("utf-8")
bytesComprimidos = zlib.compress(bytesSinComprimir)
print("Data Comprimida")
print(str(bytesComprimidos))
print("Tamaño de data comprimida: ", len(bytesComprimidos))
input("Pulsa enter para continuar")

bytesDescomprimidos = zlib.decompress(bytesComprimidos)
print("Data Descomprimida")
print(bytesDescomprimidos.decode("utf-8"))
print("Tamaño de data Descomprimida: ", len(bytesDescomprimidos))
input("Pulsa enter para continuar")
