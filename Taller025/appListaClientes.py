# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 00:06:47 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from modData import daSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQTableWidget.ui",self)
        lblRegistro = self.findChild(QtWidgets.QLabel,"lblRegistro")
        lblRegistro.setText("Total de Clientes")
        lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        tblData = self.findChild(QtWidgets.QTableWidget,"tblData")
        
        odaSQL = daSQL("Config.ini")
        df = odaSQL.EjecutarConsultaDF("uspClienteListarPy")
        nFilas = df.shape[0] #Cantidad de Filas
        nColumnas = df.shape[1] #Cantidad de Columnas
        tblData.setRowCount(nFilas)
        tblData.setColumnCount(nColumnas)
        tblData.setHorizontalHeaderLabels(df.columns.tolist())
        tblData.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
        countFila = 0
        for fila in df.itertuples():
            for celda in range(1, nColumnas + 1):
                item = QTableWidgetItem(str(fila[celda]))
                tblData.setItem(countFila, celda - 1, item)
            countFila = countFila + 1
        lblTotal.setText(str(nFilas))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
