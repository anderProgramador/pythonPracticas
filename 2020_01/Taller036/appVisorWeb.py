# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:49:00 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic, QtWebEngineWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QUrl

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgVisorWeb.ui",self)
        
        self.txtURL = self.findChild(QtWidgets.QLineEdit,"txtURL")
        self.webVisor = self.findChild(QtWebEngineWidgets.QWebEngineView,"webVisor")
        btnVerWeb = self.findChild(QtWidgets.QPushButton,"btnVerWeb")
        
        btnVerWeb.clicked.connect(self.verWeb)
        
    def verWeb(self):
        self.webVisor.setUrl(QUrl(self.txtURL.text()))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
