# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:37:29 2020

@author: Ander
"""

import sys
import pandas as pd
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QDialog, QHeaderView
from modData import daSQL
from modModelos import ModeloTabla

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQComboBox_QTableView.ui",self)
        lblData = self.findChild(QtWidgets.QLabel,"lblData")
        lblData.setText("Seleccione una Categoria")
        self.cboCategoria = self.findChild(QtWidgets.QComboBox,"cboData")
        self.tblProducto = self.findChild(QtWidgets.QTableView,"tblData")
        self.tblProducto.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
        odaSQL = daSQL("Config.ini")
        data = odaSQL.EjecutarConsultaCsv("uspCategoriaProductoListasCsvPy")
        listas = data.split("_")
        listaCategorias = listas[0].split("¬")
        listaProductos = listas[1].split("¬")
        
        self.modeloCategoria = QtGui.QStandardItemModel()
        item = QtGui.QStandardItem()
        item.setData("")
        item.setText("Todos")
        self.modeloCategoria.appendRow(item)
        campos = []
        for categoria in listaCategorias:
            campos = categoria.split("|")
            item = QtGui.QStandardItem()
            item.setData(campos[0])
            item.setText(campos[1])
            self.modeloCategoria.appendRow(item)
        self.cboCategoria.setModel(self.modeloCategoria)
        
        productos = []
        for producto in listaProductos:
            productos.append(producto.split("|"))
        self.dfProducto = pd.DataFrame(productos, columns=["Código","Nombre","Precio","Stock","IdCategoria"])
        self.tblProducto.setModel(ModeloTabla(self.dfProducto))
        
        self.cboCategoria.currentIndexChanged.connect(self.filtrarProducto)
        
    def filtrarProducto(self, index):
        modelIndex = self.modeloCategoria.index(index,0)
        item = self.modeloCategoria.itemFromIndex(modelIndex)
        codigo = item.data()
        nombre = item.text()
        
        if(codigo==""):
            dfFiltro = self.dfProducto
        else:
            dfFiltro = self.dfProducto[self.dfProducto["IdCategoria"]==codigo]
        self.tblProducto.setModel(ModeloTabla(dfFiltro))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
