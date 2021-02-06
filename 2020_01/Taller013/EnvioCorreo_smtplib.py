# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 07:33:33 2020

@author: Ander
"""

import os
import pandas as pd
import smtplib

print("Demo 13: Envio de Correos usando SMTPLIB")
try:
    ruta = "C:/Users/Ander/Documents/Python Scripts/Clases/Practicas/Archivos"
    archivoXlsx = os.path.join(ruta,"Correos.xlsx")
    df = pd.read_excel(archivoXlsx)
    nombre = df["Nombre"].tolist()
    correo = df["Correo"].tolist()
    archivoPwd = os.path.join(ruta,"PassGmail.txt")
    file = open(archivoPwd, "r")
    password = file.read()
    
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.ehlo()
    server.login("valenzuela.ander@gmail.com",password)
    print("Conexión satisfactoria")
    
    print("Enviando Correos...")
    correoDe = "valenzuela.ander@gmail.com"
    correoAsunto = "Prueba de Correo desde Python"
    correoCuerpo = "Estimad@s\n\nEste es un mensaje generado por un progama de Python\n\nFirma Ander Tu Terror"
    correoMensaje = "Subject: {0}\n\n{1}".format(correoAsunto,correoCuerpo)
    server.sendmail(correoDe,correo,correoMensaje)
    print("Se envió el correo a los sgtes personas", nombre)
except Exception as e:
    print("Error", str(e))


"""
print(df)
print(type(nombre))
print(nombre)
input("Pulsa enter para finalizar")
"""
