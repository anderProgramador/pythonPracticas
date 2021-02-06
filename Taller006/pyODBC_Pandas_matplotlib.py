# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:07:47 2020

@author: Ander
"""
import pyodbc as db
import pandas as pd
import matplotlib.pyplot as plt

con = db.connect("Driver={SQL Server};server=ANDER\SQLEXPRESS;database=BdWebDom;trusted_connection=yes")
df = pd.read_sql_query("Select Top 10 ProductName, UnitPrice, UnitsInStock From Products",con)
df.plot(x = 'ProductName', y = 'UnitPrice', kind = 'bar')
plt.show()
df.plot(x = 'ProductName', y = 'UnitsInStock', kind = 'scatter')
plt.show()
df.plot(x = 'ProductName', y = 'UnitsInStock', kind = 'line')
plt.show()
df.plot.pie(x = 'ProductName',y = 'UnitsInStock',figsize=(5,5),autopct='%1.1f%%',startangle=90)
plt.show()