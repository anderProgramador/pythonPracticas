# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 07:15:55 2020

@author: Ander
"""

import modData

class Producto:
    
    def __init__(self,archivoconfig):
        self.daSQL = modData.daSQL("Config.ini")

    def ListarCsv(self):
        csv = self.daSQL.EjecutarConsultaCsv("uspProductoListarCsv")
        return csv

    def ListarDF(self):
        df = self.daSQL.EjecutarConsultaDF("uspProductoListar")
        return df

    def ObtenerPorIdCsv(self, idProducto):
        csv = self.daSQL.EjecutarConsultaCsv("uspProductoObtenerPorIdCsv","Data",idProducto)
        return csv

    def ObtenerPorIdDF(self, idProducto):
        df = self.daSQL.EjecutarConsultaDF("uspProductoObtenerPorId","ProductId",idProducto)
        return df

    def AdicionarCsv(self, nombre, idProveedor, idCategoria, precio, stock, disc):
        data = "|{0}|{1}|{2}|{3}|{4}|{5}".format(nombre, idProveedor, idCategoria, precio, stock, disc)
        n = self.daSQL.EjecutarComando("uspProductoGrabarCsv","Data",data)
        return n

    def ActualizarCsv(self, codigo, nombre, idProveedor, idCategoria, precio, stock, disc):
        data = "|{0}|{1}|{2}|{3}|{4}|{5}|{6}".format(codigo, nombre, idProveedor, idCategoria, precio, stock, disc)
        n = self.daSQL.EjecutarComando("uspProductoGrabarCsv","Data",data)
        return n

    def EliminarCsv(self, codigo):
        n = self.daSQL.EjecutarComando("uspProductoEliminarPorIdCsv","Data",codigo)
        return n
    