# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:19:38 2020

@author: Ander
"""
from urllib.request import urlopen
import json

print("Demo 06: urllib y json para consulta de ruc sunat")
uri = "https://api.sunat.cloud/ruc/"
ruc = input("Ingrese el RUC a consultar: ")
rpta = urlopen(uri + ruc)
#print(type(rpta))
data = rpta.read()
#print(data)
#print(type(data))
obj = json.loads(data)
#print(type(obj))
print("Razon Social", obj["razon_social"])
print("Fecha Actividad", obj["fecha_actividad"])
print("Contribuyente Condicion", obj["contribuyente_condicion"])
print("Contribuyente Estado", obj["contribuyente_estado"])
input("Pulsa una tecla para finalizar")
