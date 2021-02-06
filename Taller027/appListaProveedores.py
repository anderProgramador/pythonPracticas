# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:20:33 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog
from modData import daSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQListView.ui",self)
        lblRegistro = self.findChild(QtWidgets.QLabel,"lblRegistro")
        lblRegistro.setText("Total de Proveedores")
        lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        lvwData = self.findChild(QtWidgets.QListView,"lvwData")
        
        odaSQL = daSQL("Config.ini")
        df = odaSQL.EjecutarConsultaDF("uspProveedorListarPy")
        proveedores = df["CompanyName"].tolist()
        modelo = QtCore.QStringListModel()
        modelo.setStringList(proveedores)
        lvwData.setModel(modelo)
        lblTotal.setText(str(len(proveedores)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
