# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:29:14 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQColumnView.ui",self)
        self.lblRuta = self.findChild(QtWidgets.QLabel,"lblRuta")
        cvwData = self.findChild(QtWidgets.QColumnView,"cvwData")
        cvwData.doubleClicked.connect(self.mostrarRuta)
        self.modelo = QtWidgets.QDirModel()
        cvwData.setModel(self.modelo)
        
    def mostrarRuta(self, value):
        self.setWindowTitle("fila: {0} - columna: {1} - valor: {2}".format(value.row(), value.column(), value.data()))
        self.lblRuta.setText(self.modelo.filePath(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
