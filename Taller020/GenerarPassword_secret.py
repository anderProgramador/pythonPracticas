# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:20:35 2020

@author: Ander
"""

import string
import secrets

print("Demo 20: Generar códigos o claves con Reglas usando secrets")
n = int(input("Ingresa el tamaño del password: "))
d = int(input("Ingresa el mínimo nùmero de digitos: "))
m = int(input("Ingresa el mínimo número de mayúsculas: "))

cadena = string.ascii_letters + string.digits

while True:
    password = ''.join(secrets.choice(cadena) for i in range(n))
    if(any(c.islower() for c in password)
           and sum(c.isupper()for c in password) >= m
           and sum(c.isdigit() for c in password) >= d):
        break

print("\nPassword: ", password)
print("Tamaño: ", len(password))
           
