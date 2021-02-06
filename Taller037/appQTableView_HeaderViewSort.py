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

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQTableView.ui",self)
        self.setWindowTitle("Ordenación en Lista de Productos")
        
        tblProducto = self.findChild(QtWidgets.QTableView,"tblData")
        lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        
        # Llenar el DataFrame con la data de Productos
        objProducto = Producto("Config.ini")
        df = objProducto.ListarDF()
        # Crear el Modelo desde el DataFrame
        modeloProducto = ModeloTabla(df)
        # Crear un proxy para que el modelo se pueda ordenar
        proxy = QtCore.QSortFilterProxyModel()
        proxy.setSourceModel(modeloProducto)
        # Enlazar el Proxy al QTableView
        tblProducto.setModel(proxy)
        # Configurar el QTableView para que se habilite la ordenación
        tblProducto.setSortingEnabled(True)
        # Configurar que se ordene ascendente por Codigo
        tblProducto.sortByColumn(0, Qt.AscendingOrder)
        # Autoajustar los anchos de columnas
        tblProducto.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Mostrar el total de registros
        lblTotal.setText(str(df.shape[0]))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
