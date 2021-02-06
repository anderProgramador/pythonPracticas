# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 07:36:33 2020

@author: Ander
"""

from modProducto import Producto

print("Demo de Mantenimiento de Productos usando Módulos")
opcion = ""

while(opcion!="6"):
    print("[1] Listar Todos los Productos")
    print("[2] Consultar por Codigo")
    print("[3] Adicionar Producto")
    print("[4] Actualizar Producto")
    print("[5] Eliminar Producto")
    print("[6] Salie")
    opcion = input("Selecciona una opción: ")
    objProducto = Producto("Config.ini")
    if(opcion=="1"):
        data = objProducto.ListarCsv()
        print(data)
    if(opcion=="2"):
        codigo = input("Código del Producto a Consultar: ")
        data = objProducto.ObtenerPorIdCsv(codigo)
        print(data)
    if(opcion=="3"):
        nombre = input("Nombre del Producto: ")
        idProveedor = input("Código del Proveedor: ")
        idCategoria = input("Código de la Categoria: ")
        precio = input("Precio Unitario: ")
        stock = input("Stock del Producto: ")
        disc = input("Dscto del Producto: ")
        n = objProducto.AdicionarCsv(nombre,idProveedor,idCategoria,precio,stock,disc)
        print("Se adicionó {0} registros".format(n))
    if(opcion=="4"):
        codigo = input("Código del Producto a Actualizar: ")
        nombre = input("Nombre del Producto: ")
        idProveedor = input("Código del Proveedor: ")
        idCategoria = input("Código de la Categoria: ")
        precio = input("Precio Unitario: ")
        stock = input("Stock del Producto: ")
        disc = input("Dscto del Producto: ")
        n = objProducto.ActualizarCsv(codigo,nombre,idProveedor,idCategoria,precio,stock,disc)
        print("Se actualizo {0} registros".format(n))
    if(opcion=="5"):
        codigo = input("Código del Producto a Eliminar: ")
        n = objProducto.EliminarCsv(codigo)
        print("Se elimino {0} registros".format(n))

