import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage, QTimeEdit, QMainWindow
from PyQt5.QtCore import QTimer, QTime
from PyQt5.uic import loadUi
import mysql.connector
from tkinter import *
from datetime import datetime
import threading
app = QtWidgets.QApplication([])

menu = False

# Função Menu tela inicial
def function_menu():
    global menu
    if(menu == False):
        inicio.widgetMenu.show()
        menu = True
    else:
        inicio.widgetMenu.hide()
        menu = False

#tela inicial
inicio = uic.loadUi("telas/tela_menu.ui")
pushMenu = inicio.pushMenu.clicked.connect(function_menu)
#pushVendas = inicio.pushVendas.clicked.connect()
#pushEstoque = inicio.pushEstoque.clocked.connect()

inicio.widgetMenu.hide()
inicio.show()
app.exec_()