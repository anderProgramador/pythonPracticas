# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 22:23:55 2020

@author: Ander
"""

import configparser
import pyodbc
import pandas as pd

class daSQL:
    def __init__(self, archivoconfig): #Constructor con parametros
        try:
            config = configparser.ConfigParser()
            config.read(archivoconfig)
            driver = config.get("CoreContext","driver")
            server = config.get("CoreContext","server")
            database = config.get("CoreContext","database")
            user = config.get("CoreContext","user")
            password = config.get("CoreContext","password")
            self.CadenaConexion = "Driver={0};server={1};database={2};user={3};password={4}".format(driver,server,database,user,password)
        except Exception as error:
            print("Error Constructor: {0}".format(str(error)))
        
    def EjecutarConsultaCsv(self,nombreSP,nombreParametro="",valorParametro=""):
        rpta = ""
        try:
            conn = pyodbc.connect(self.CadenaConexion)
            cursor = conn.cursor()
            if(nombreParametro!="" and valorParametro!=""):
                cursor.execute("exec {0} @{1}={2}".format(nombreSP,nombreParametro,valorParametro))
            else:
                cursor.execute(nombreSP)
            rpta = cursor.fetchval()
            cursor.close()
            conn.close()
        except  Exception as error:
            print("Error EjecutarConsultaCsv: {0}".format(str(error)))
        return rpta
        
    def EjecutarConsultaDF(self,nombreSP,nombreParametro="",valorParametro=""):
        df = ""
        try:
            conn = pyodbc.connect(self.CadenaConexion)
            if(nombreParametro!="" and valorParametro!=""):
                df = pd.read_sql_query("exec {0} @{1}={2}".format(nombreSP,nombreParametro,valorParametro),conn)
            else:
                df = pd.read_sql_query(nombreSP,conn)
            conn.close()
        except  Exception as error:
            print("Error EjecutarConsultaDF: {0}".format(str(error)))
        return df
        
    def EjecutarComando(self,nombreSP,nombreParametro="",valorParametro=""):
        rpta = 0
        try:
            conn = pyodbc.connect(self.CadenaConexion)
            cursor = conn.cursor()
            if(nombreParametro!="" and valorParametro!=""):
                rpta = cursor.execute("exec {0} @{1}=?".format(nombreSP,nombreParametro),valorParametro).rowcount
            else:
                rpta = cursor.execute(nombreSP).rowcount
            cursor.commit()
            cursor.close()
            conn.close()
        except  Exception as error:
            print("Error EjecutarComando: {0}".format(str(error)))
        return rpta

'''    
class daORACLE:
    print("Error EjecutarConsultaCsv: ", error)
'''
    