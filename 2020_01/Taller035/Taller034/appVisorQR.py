# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:21:48 2020

@author: Ander
"""

import sys
# import os
import cv2
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QPixmap

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgVisorQR.ui",self)
        
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
        dlg.setNameFilters(["Archivos png (*.png)","Archivos jpg (*.jpg)","Archivos Mapa de Bits (*.bmp)"])
        if dlg.exec_():
            archivos = dlg.selectedFiles()
            self.txtArchivo.setText(archivos[0])
            self.lblImagen.setPixmap(QPixmap(archivos[0]))
            
            image = cv2.imread(archivos[0])
            objQR = cv2.QRCodeDetector()
            codigo, puntos, _ = objQR.detectAndDecode(image)
            if puntos is not None:
                self.lblMensaje.setText("Código QR: {0}".format(codigo))
            else:
                self.lblMensaje.setText("Código QR: No detectado")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())