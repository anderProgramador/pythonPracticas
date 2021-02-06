# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:21:48 2020

@author: Ander
"""

import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QPixmap

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgVisorImagen.ui",self)
        
        self.txtArchivo = self.findChild(QtWidgets.QLineEdit,"txtArchivo")
        btnAbrir = self.findChild(QtWidgets.QPushButton,"btnAbrir")
        self.lblImagen = self.findChild(QtWidgets.QLabel,"lblImagen")
        self.lblImagen.setScaledContents(True)
        self.lblMensaje = self.findChild(QtWidgets.QLabel,"lblMensaje")
        
        btnAbrir.clicked.connect(self.abrirDialgoArchivo)
        
    def abrirDialgoArchivo(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setDirectory("C:/Users/Ander/Pictures")
        dlg.setNameFilters(["Archivos jpg (*.jpg)","Archivos png (*.png)","Archivos Mapa de Bits (*.bmp)"])
        if dlg.exec_():
            archivos = dlg.selectedFiles()
            self.lblMensaje.setText("Nombre Archivo: {0}".format(os.path.basename(archivos[0])))
            self.txtArchivo.setText(archivos[0])
            self.lblImagen.setPixmap(QPixmap(archivos[0]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())