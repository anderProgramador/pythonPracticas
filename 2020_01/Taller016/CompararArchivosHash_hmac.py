# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 07:10:47 2020

@author: Ander
"""

import os
import hmac

print("Demo 16: Comparación de archivos usando Hash HMAC")
archivoOriginal = input("Ingresa el archivo original: ")
if(os.path.isfile(archivoOriginal)):
    archivoComparar = input("Ingresa el archivo a comparar: ")
    if(os.path.isfile(archivoOriginal)):
        fileOriginal = open(archivoOriginal,"rb")
        sizeOriginal = os.stat(archivoOriginal).st_size
        fileComparar = open(archivoComparar,"rb")
        sizeComparar = os.stat(archivoComparar).st_size
        if(sizeOriginal == sizeComparar):
            dataOriginal = fileOriginal.read()
            dataComparar = fileComparar.read()
            hashOriginal = hmac.new(dataOriginal).digest()
            hashComparar = hmac.new(dataComparar).digest()
            if(hashOriginal == hashComparar):
                print("Los contenidos son iguales")
            else:
                print("Los contenidos son diferentes")
        else:
            print("Los archivos son de diferente tamaño")
        
    