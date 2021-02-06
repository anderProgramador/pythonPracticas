# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:02:52 2020

@author: Ander
"""

from PyQt5 import QtGui

class ModeloEstandar:
    def Enlazar(self, df, tbl):
        nColumnas = df.shape[1] #Cantidad de Columnas
        
        modelo = QtGui.QStandardItemModel()
        modelo.setHorizontalHeaderLabels(df.columns.tolist())
        
        countFila = 0
        for fila in df.itertuples():
            row = []
            for columna in range(1, nColumnas + 1):
                celda = QtGui.QStandardItem(str(fila[columna]))
                row.append(celda)
            modelo.appendRow(row)
            countFila = countFila + 1
        
        tbl.setModel(modelo)
