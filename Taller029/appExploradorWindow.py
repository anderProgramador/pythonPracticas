# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:36:57 2020

@author: Ander
"""

import sys
import os
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQTreeView.ui",self)
        self.lblRuta = self.findChild(QtWidgets.QLabel,"lblRuta")
        tvwData = self.findChild(QtWidgets.QTreeView,"tvwData")
        tvwData.doubleClicked.connect(self.mostrarRuta)
        self.modelo = QtWidgets.QFileSystemModel()
        self.modelo.setRootPath(QtCore.QDir.currentPath())
        tvwData.setModel(self.modelo)
        tvwData.setColumnWidth(0,450)
        tvwData.setColumnWidth(1,70)
        tvwData.setColumnWidth(2,150)
        tvwData.setColumnWidth(3,200)
        
    def mostrarRuta(self, value):
        archivo = self.modelo.filePath(value)
        self.lblRuta.setText(archivo)
        os.system("start " + archivo)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
