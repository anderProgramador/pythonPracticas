# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:21:10 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QListWidgetItem
from modData import daSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQListWidget.ui",self)
        lblRegistro = self.findChild(QtWidgets.QLabel,"lblRegistro")
        lblRegistro.setText("Total de Proveedores")
        lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        lvwData = self.findChild(QtWidgets.QListWidget,"lvwData")
        
        odaSQL = daSQL("Config.ini")
        df = odaSQL.EjecutarConsultaDF("uspProveedorListarPy")
        proveedores = df["CompanyName"].tolist()
        for proveedor in proveedores:
            item = QListWidgetItem(proveedor)
            lvwData.addItem(item)
        lblTotal.setText(str(len(proveedores)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
