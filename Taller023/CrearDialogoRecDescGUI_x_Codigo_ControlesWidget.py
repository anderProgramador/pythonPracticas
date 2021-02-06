# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:55:40 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QMessageBox
from modProducto import Producto

class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("frmProducto.ui",self)
        
        self.lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        self.lvwProducto = self.findChild(QtWidgets.QListWidget,"lvwProducto")
        self.bntExportarExcel = self.findChild(QtWidgets.QPushButton,"bntExportarExcel")
        self.bntExportarExcel.clicked.connect(self.exportarExcel)
        self.txtNombre = self.findChild(QtWidgets.QLineEdit,"txtNombre")
        self.txtNombre.textChanged.connect(self.consultarProductos)
        self.btnSalir = self.findChild(QtWidgets.QPushButton,"btnSalir")
        self.btnSalir.clicked.connect(self.salir)
        
        self.lvwProducto.clear()
        objProducto = Producto("Config.ini")
        self.data = objProducto.ListarDF()
        nombres = self.data["ProductName"].tolist()
        
        for nombre in nombres:
            item = QListWidgetItem(nombre)
            self.lvwProducto.addItem(item)
       
        self.lblTotal.setText(str(len(nombres)))
    
    def exportarExcel(self):
        self.data.to_excel("Producto.xlsx", index=False)
        msg = QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText("El archivo excel fue creado")
        msg.exec_()
        
    def consultarProductos(self,valorTexto):
        self.lvwProducto.clear()
        filtro = self.data[self.data["ProductName"].str.contains(valorTexto)]
        nombres = filtro["ProductName"].tolist()
        for nombre in nombres:
            item = QListWidgetItem(nombre)
            self.lvwProducto.addItem(item)
        self.lblTotal.setText(str(len(nombres)))
        
    def salir(self):
        self.close()
       
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frm = Ventana()
    frm.show()
    sys.exit( app.exec_())
        
