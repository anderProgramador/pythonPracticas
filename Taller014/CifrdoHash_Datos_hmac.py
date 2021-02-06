# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 06:23:09 2020

@author: Ander
"""

import hmac

print("Demo 14: Cifrado Hash usando HMAC")
mensaje = input("Ingrese el mensaje a cifrar: ")
print("Mensaje en Texto", mensaje)
print("Tamaño del Mensaje", len(mensaje))
buffer = mensaje.encode("utf-8")
print("Mensaje en Bytes", buffer)

objHash = hmac.new(buffer)
mensajeCifrado = objHash.digest()
#print(type(mensajeCifrado))
print("Mensaje Cifrado", mensajeCifrado)
print("Mensaje Cifrado Hash HMAC", str(mensajeCifrado))
print("Tamaño del Mensaje Cifrado Hash HMAC", len(mensajeCifrado))

mensajeCifradoHex = objHash.hexdigest()
#print(type(mensajeCifrado))
print("Mensaje Cifrado", mensajeCifradoHex)
print("Mensaje Cifrado Hash HMAC Hex", str(mensajeCifradoHex))
print("Tamaño del Mensaje Cifrado Hash HMAC Hex", len(mensajeCifradoHex))
