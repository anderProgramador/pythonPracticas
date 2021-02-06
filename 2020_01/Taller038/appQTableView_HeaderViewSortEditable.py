# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 23:33:56 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog, QHeaderView
from PyQt5.QtCore import Qt
from modProducto import Producto
from modModelos import ModeloTabla
from modHeaderView import EditableHeaderView

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQTableView.ui",self)
        self.setWindowTitle("Ordenación y Filtro en Lista de Productos")
        
        tblProducto = self.findChild(QtWidgets.QTableView,"tblData")
        self.lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        
        # Llenar el DataFrame con la data de Productos
        objProducto = Producto("Config.ini")
        df = objProducto.ListarDF()
        # Crear una cabecera editable
        headerView = EditableHeaderView(tblProducto)
        tblProducto.setHorizontalHeader(headerView)
        # Crear el Modelo desde el DataFrame
        modeloProducto = ModeloTabla(df)
        # Crear un proxy para que el modelo se pueda ordenar
        self.proxy = QtCore.QSortFilterProxyModel()
        self.proxy.setSourceModel(modeloProducto)
        # Enlazar el Proxy al QTableView
        tblProducto.setModel(self.proxy)
        # Configurar el QTableView para que se habilite la ordenación
        tblProducto.setSortingEnabled(True)
        # Configurar que se ordene ascendente por Codigo
        tblProducto.sortByColumn(0, Qt.AscendingOrder)
        # Autoajustar los anchos de columnas
        tblProducto.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Mostrar el total de registros
        self.lblTotal.setText(str(df.shape[0]))
        
        # Configurar todas las columnas editables
        nCols = df.shape[1]
        for i in range(nCols):
            headerView.setEditable(i, True)
        
        # Configurar para que al escribir texto en la cabecera se pueda filtrar
        headerView.textChanged.connect(self.filtrarProductos)
        
    def filtrarProductos(self, indiceColumna, valorTexto):
        self.proxy.setFilterKeyColumn(indiceColumna)
        self.proxy.setFilterWildcard("*{0}".format(valorTexto) if valorTexto else "")
        self.lblTotal.setText(str(self.proxy.rowCount()))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
