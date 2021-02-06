# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:13:24 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QHeaderView, QAbstractItemView
from modData import daSQL
from modModelos import ModeloEstandar

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQTableView.ui",self)
        lblRegistro = self.findChild(QtWidgets.QLabel,"lblRegistro")
        lblRegistro.setText("Total de Proveedores")
        lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        tblData = self.findChild(QtWidgets.QTableView,"tblData")
        
        odaSQL = daSQL("Config.ini")
        df = odaSQL.EjecutarConsultaDF("uspProveedorListarPy")
        nFilas = df.shape[0] #Cantidad de Filas
        
        ModeloEstandar().Enlazar(df,tblData)
        
        tblData.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        tblData.setSelectionBehavior(QAbstractItemView.SelectRows)
        lblTotal.setText(str(nFilas))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())