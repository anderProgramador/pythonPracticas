# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 07:26:35 2020

@author: Ander
"""

import os #os.path.isdir, os.listdir
import shutil #shutil.copy()

print("Demo 009: Sentencias de flujo for, if  & Módulos Estándar: os, shutil")
directorioOrigen = input("Ingrese el directorio origen: ")
if directorioOrigen != "" and os.path.isdir(directorioOrigen):
    directorioDestino = input("Ingrese el directorio destino: ")
    if directorioDestino != "" and os.path.isdir(directorioDestino):
        archivos = os.listdir(directorioOrigen)
        for nombre in archivos:
            print("Copiando ", nombre)
            archivoOrigen = os.path.join(directorioOrigen, nombre)
            archivoDestino = os.path.join(directorioDestino, nombre)
            shutil.copy(archivoOrigen, archivoDestino)
        print("Se copiaron: {0} archivos".format(len(archivos)))
    else:
        print("Directorio destino no existe o esta vacio")
else:
    print("Directorio origen no existe o esta vacio")
input("Pulsa enter para finalizar")