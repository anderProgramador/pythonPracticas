# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 00:21:35 2020

@author: Ander
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem
from modData import daSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgQTreeWidget.ui",self)
        lblRegistro = self.findChild(QtWidgets.QLabel,"lblRegistro")
        lblRegistro.setText("Total de Ubigeo")
        lblTotal = self.findChild(QtWidgets.QLabel,"lblTotal")
        tvwData = self.findChild(QtWidgets.QTreeWidget,"tvwData")
        tvwData.setColumnCount(2)
        tvwData.setColumnWidth(0,400)
        tvwData.setColumnWidth(1,400)
        tvwData.setHeaderLabels(["Codigo del Ubigeo","Nombre del Ubigeo"])
        
        odaSQL = daSQL("Config.ini")
        data = odaSQL.EjecutarConsultaCsv("uspUbigeoListarCsvPy")
        lista = data.split(";")
        for linea in lista:
            codigoUbigeo = linea[:6]
            nombreUbigeo = linea[6:]
            if(codigoUbigeo[:2]!="00" and codigoUbigeo[2:4]=="00" and codigoUbigeo[4:]=="00"):
                dpto = QTreeWidgetItem([codigoUbigeo, nombreUbigeo])
                tvwData.addTopLevelItem(dpto)
            if(codigoUbigeo[:2]!="00" and codigoUbigeo[2:4]!="00" and codigoUbigeo[4:]=="00"):
                prov = QTreeWidgetItem([codigoUbigeo, nombreUbigeo])
                dpto.addChild(prov)
            if(codigoUbigeo[:2]!="00" and codigoUbigeo[2:4]!="00" and codigoUbigeo[4:]!="00"):
                dist = QTreeWidgetItem([codigoUbigeo, nombreUbigeo])
                prov.addChild(dist)
        lblTotal.setText(str(len(lista)))
        tvwData.expandAll()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
