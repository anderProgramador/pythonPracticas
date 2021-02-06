# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:55:40 2020

@author: Ander
"""

#from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QWidget, QGridLayout
from PyQt5.QtCore import QSize
from modProducto import Producto

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setMinimumSize(QSize(840,680))
        self.setWindowTitle("Lista de Productos")
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        
        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)
        
        objProducto = Producto("Config.ini")
        df = objProducto.ListarDF()
        nombres = df["ProductName"].tolist()
        
        lvwProducto = QListWidget(self)
        lvwProducto.setObjectName("lvwProducto")
        for nombre in nombres:
            item = QListWidgetItem(nombre)
            lvwProducto.addItem(item)
        gridLayout.addWidget(lvwProducto,0,0)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frm = Ventana()
    frm.show()
    sys.exit( app.exec_())
        
