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
#print(type(con))
cursor = con.cursor()
#print(type(cursor))
cursor.execute("Select ProductId, ProductName, UnitPrice, UnitsInStock from Products")
#cursor.execute("Select * from Products")
#cursor.execute("Select * from Employees")
#cursor.execute("Select * from Cubso")
horaFin = dt.datetime.now()
tiempo1 = horaFin - horaInicio
#print(type(horaFin))
#print(type(tiempo))

archivo = "Productos.txt"
file = open(archivo,"w")
file.write("ProductId ProductName UnitPrice UnitsInStock\n")
horaInicio = dt.datetime.now()
for fila in cursor:
    #print(type(fila))
    #file.write(str(fila))
    for celda in fila:
        print(celda)
        file.write(str(celda))
        file.write(", ")
    print("_____________")
    file.write("\n")
horaFin = dt.datetime.now()
tiempo2 = horaFin - horaInicio
file.close()

print("Tiempo de Conexion ", tiempo1.total_seconds() * 1000, " msg")
print("Tiempo de Pintado y archivo ", tiempo2.total_seconds() * 1000, " msg")

