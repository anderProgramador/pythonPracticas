# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:36:11 2020

@author: Ander
"""

import pyodbc as db
import datetime as dt
import pandas as pd

print("Demo 04: pyodbc, Pandas, archivos: txt, csv, zip, html, xlsx, docx")

horaInicio = dt.datetime.now()
con = db.connect("Driver={SQL Server};server=ANDER\SQLEXPRESS;database=BdWebDom;trusted_connection=yes")
#df = pd.read_sql_query("uspProductoListarCsv",con)
df = pd.read_sql_query("Select ProductId,ProductName,UnitPrice,UnitsInStock from Products",con)
horaFin = dt.datetime.now()
tiempo1 = horaFin - horaInicio

horaInicio = dt.datetime.now()
print(df)
archivo = "Productos"
df.to_csv(archivo + ".txt",index=False)
df.to_excel(archivo + ".xlsx",index=False)
df.to_html(archivo + ".html",index=False)
df.to_json(archivo + ".json",index=False,orient ="table")
comp_opc = dict(method='zip',archive_name=archivo + ".txt")
df.to_csv(archivo + ".zip",index=False,compression = comp_opc)

horaFin = dt.datetime.now()
tiempo2 = horaFin - horaInicio

print("Tiempo de Conexion Pandas SP ", tiempo1.total_seconds() * 1000, " msg")
print("Tiempo de Pintado y archivo ", tiempo2.total_seconds() * 1000, " msg")

