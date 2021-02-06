# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:09:06 2020

@author: Ander
"""

import modData

print("Prueba del Modulo de Acceso a Datos")
odaSQL = modData.daSQL("Config.ini")
#data = odaSQL.EjecutarConsultaCsv("uspProductoListarCsv")
#if(data):
    #print(data)
#data = odaSQL.EjecutarConsultaDF("uspProductoListar")
#print(data)
datos = "20252|Dormilones|4|2|3|100|0"
n = odaSQL.EjecutarComando("uspProductoGrabarCsv","Data",datos)
print("Se actualizo registros: ", n)

