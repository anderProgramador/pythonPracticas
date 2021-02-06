# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 06:47:53 2020

@author: Ander
"""

import hashlib

print("Demo 15: Cifrado Hash SHA256 usando HASHLIB")
mensaje = input("Ingrese el mensaje a cifrar: ")
buffer = mensaje.encode("utf-8")
print("Mensaje en Texto", mensaje)
print("Tamaño del Mensaje", len(mensaje))
print("Mensaje en Bytes", buffer)

objHash = hashlib.sha256()
objHash.update(buffer)
mensajeCifrado = objHash.digest()
#print(type(mensajeCifrado))
print("Mensaje Cifrado Hash HMAC", str(mensajeCifrado))
print("Tamaño del Mensaje Cifrado Hash HMAC", len(mensajeCifrado))

mensajeCifradoHex = objHash.hexdigest()
#print(type(mensajeCifrado))
print("Mensaje Cifrado Hash HMAC Hex", str(mensajeCifradoHex))
print("Tamaño del Mensaje Cifrado Hash HMAC Hex", len(mensajeCifradoHex))
