# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:37:29 2020

@author: Ander
"""

import sys
import pandas as pd
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from matplotlib.pylab import plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from modData import daSQL
from modModelos import ModeloTabla

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgGrafico.ui",self)
        self.cboTipoGrafico = self.findChild(QtWidgets.QComboBox,"cboTipoGrafico")
        self.cboCategoria = self.findChild(QtWidgets.QComboBox,"cboCategoria")
        self.btnGrabar = self.findChild(QtWidgets.QPushButton,"btnGrabar")
        self.imgGrafico = self.findChild(QtWidgets.QWidget,"imgGrafico")
        self.layout = QtWidgets.QVBoxLayout(self.imgGrafico)
        
        # Obtener Datos y crear dos listas: Categorias y Productos
        odaSQL = daSQL("Config.ini")
        data = odaSQL.EjecutarConsultaCsv("uspCategoriaProductoListasCsvPy")
        listas = data.split("_")
        listaCategorias = listas[0].split("¬")
        listaProductos = listas[1].split("¬")
        
        # Llenar el combo de tipos de graficos
        tiposGraficos = ["Seleccione", "line","bar", "barh", "hist", "box", "kde", "density", "area", "pie"]
        modeloTipoGrafico = QtCore.QStringListModel()
        modeloTipoGrafico.setStringList(tiposGraficos)
        self.cboTipoGrafico.setModel(modeloTipoGrafico)
        
        # Llenar el combo de categorias con array de listas
        self.modeloCategoria = QtGui.QStandardItemModel()
        item = QtGui.QStandardItem()
        item.setData("")
        item.setText("Seleccione")
        self.modeloCategoria.appendRow(item)
        campos = []
        for categoria in listaCategorias:
            campos = categoria.split("|")
            item = QtGui.QStandardItem()
            item.setData(campos[0])
            item.setText(campos[1])
            self.modeloCategoria.appendRow(item)
        self.cboCategoria.setModel(self.modeloCategoria)
        
        # Crear un DataFrame con la lista de Productos
        productos = []
        for producto in listaProductos:
            productos.append(producto.split("|"))
        self.df = pd.DataFrame(data = productos,columns = ["Código","Nombre","Precio","Stock","Id Categoria"])
        self.df["Stock"] = pd.to_numeric(self.df["Stock"])
        
        # Programar eventos de los controles
        self.cboTipoGrafico.currentIndexChanged.connect(self.graficarProducto)
        self.cboCategoria.currentIndexChanged.connect(self.graficarProducto)
        self.btnGrabar.clicked.connect(self.grabarGrafico)
        
    def graficarProducto(self, index):
        # Obtener el tipo de grafico seleccionado
        tipoGrafico = self.cboTipoGrafico.currentText()
        
        # Obtener ek codigo y nombre de la categoria seleccionada
        indiceCategoria = self.cboCategoria.currentIndex()
        indiceModeloCategoria = self.modeloCategoria.index(indiceCategoria, 0)
        item = self.modeloCategoria.itemFromIndex(indiceModeloCategoria)
        codigoCategoria = item.data()
        # nombreCategoria = item.text()
        
        # Filtrar y Graficar
        if(tipoGrafico != "Seleccione" and codigoCategoria != ""):
            figura, ejes = plt.subplots()
            filtro = self.df[self.df["Id Categoria"]==codigoCategoria]
            self.grafico = filtro.plot(x="Nombre", y="Stock",kind=tipoGrafico, ax=ejes).get_figure()
            canvas = FigureCanvas(figura)
            if(self.layout.count()>0):
                self.layout.itemAt(0).widget().setParent(None)
            self.layout.addWidget(canvas)
            
    def grabarGrafico(self):
        tipoGrafico = self.cboTipoGrafico.currentText()
        nombreCategoria = self.cboCategoria.currentText()
        dlg = QMessageBox()
        dlg.setWindowTitle("Aviso")
        if(hasattr(self,"grafico")):
            self.grafico.savefig("Grafico de {0} para {1}.png".format(tipoGrafico,nombreCategoria))
            dlg.setText("Se creo el archivo con el gráfico")
        else:
            dlg.setText("No hay nada que graficar")
        dlg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialogo()
    dlg.show()
    sys.exit( app.exec_())
