# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:02:52 2020

@author: Ander
"""

from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractTableModel, Qt

class ModeloEstandar:
    def EnlazarDataFrame(self, df, tbl):
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

class ModeloTabla(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
        
    def rowCount(self, parent=None):
        return self._data.shape[0]
    
    def columnCount(self, parent=None):
        return self._data.shape[1]
    
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None
    
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
