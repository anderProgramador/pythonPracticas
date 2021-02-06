# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:36:11 2020

@author: Ander
"""

import pyodbc as db
import datetime as dt

print("Demo 02: pyodbc, ejecutar SQL, cursor, tiempos, archivos")
horaInicio = dt.datetime.now()
con = db.connect("Driver={SQL Server};server=ANDER\SQLEXPRESS;database=BdWebDom;trusted_connection=yes")
cursor = con.cursor()
cursor.execute("uspProductoListarCsv")
horaFin = dt.datetime.now()
tiempo1 = horaFin - horaInicio

archivo = "Productos.txt"
file = open(archivo,"w")
horaInicio = dt.datetime.now()
data = cursor.fetchval().replace("¬","\n").replace("|",",")
print(data)
file.write(data)
file.close()

horaFin = dt.datetime.now()
tiempo2 = horaFin - horaInicio

print("Tiempo de Conexion ", tiempo1.total_seconds() * 1000, " msg")
print("Tiempo de Pintado y archivo ", tiempo2.total_seconds() * 1000, " msg")

