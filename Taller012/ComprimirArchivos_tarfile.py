# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 07:15:53 2020

@author: Ander
"""

import tarfile
import os

print("Demo 12: Comprimir archivos usando la librería tarfile")
directorioOrigen = input("Ingresa directorio con los archivos a comprimir: ")
if(os.path.isdir(directorioOrigen)):
    archivos = os.listdir(directorioOrigen)
    #archivoComprimir = "C:/Users/Ander/Documents/Python Scripts/Clases/Practicas/Archivos/Comprimidos/Comprimidos.zip"
    archivoComprimir = "C:/Users/Ander/Documents/Python Scripts/Clases/Practicas/Archivos/Comprimidos/Comp2.tar"
    tarC = tarfile.open(archivoComprimir,"w")
    for nombre in archivos:
        archivo = os.path.join(directorioOrigen,nombre)
        print("Comprimiendo: ", nombre)
        tarC.add(archivo)
    tarC.close()
    print("Se comprimio: {0}".format(len(archivos)))
    input("Pulsa enter para Descomprimir")
    rutaDescomprimir = "../Archivos/Descomprimidos"
    tarD = tarfile.open(archivoComprimir,"r")
    tarD.extractall(rutaDescomprimir)
    listaComprimida = tarD.getnames()
    #for archivo in listaComprimida:
    #    print("Descomprimiendo ", os.path.basename(archivo))
    tarD.close()
    print("Se descomprimio: {0}".format(len(listaComprimida)))
else:
    print("No existe el Directorio")

