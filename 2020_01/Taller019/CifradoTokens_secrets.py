# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:07:19 2020

@author: Ander
"""

import secrets

def convertirBytesToString(buffer):
    rpta=""
    for byte in buffer:
        rpta += chr(byte)
    return rpta

print("Demo 19: Crear tokens usando secrets")
nbytes = int(input("Ingresa tamaño de bytes: "))

bytesToken = secrets.token_bytes(nbytes)
print("Token Bytes: ", bytesToken)
print("Token String: ", convertirBytesToString(bytesToken))
print("Token Tamaño: ", len(bytesToken))

stringHexToken = secrets.token_hex(nbytes)
print("Token Hex Bytes: ", stringHexToken)
print("Token Hex Tamaño: ", len(stringHexToken))

stringUrlToken = secrets.token_urlsafe(nbytes)
print("Token URL Bytes: ", stringUrlToken)
print("Token URL Tamaño: ", len(stringUrlToken))

