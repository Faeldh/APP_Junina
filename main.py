import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage, QTimeEdit, QMainWindow
from PyQt5.QtCore import QTimer, QTime
from PyQt5.uic import loadUi
import mysql
import mysql.connector
from tkinter import *
from datetime import datetime
import threading
app = QtWidgets.QApplication([])

menu = False
estoque = [
    #0  1   2   3   4   5
    [0, "Água", 4,00],
    [1, "Suco", 6,00],
    [2, "Comida", 10,00],
    [3, "Brinquedo", 25,00]
]
vendas = []

# Função Menu tela inicial
def function_menu():
    global menu
    if(menu == False):
        inicio.widgetMenu.show()
        menu = True
    else:
        inicio.widgetMenu.hide()
        menu = False

def estoque():
    tela_estoque.show()
    inicio.close()

def vendas():
    tela_vendas.show()
    inicio.close()

def tela_inicio():
    inicio.show()
    tela_estoque.close()
    tela_vendas.close()

#def vendaPesquisa():


#tela inicial
inicio = uic.loadUi('telas/tela_menu.ui')
tela_estoque = uic.loadUi('telas/tela_estoque.ui')
tela_vendas = uic.loadUi('telas/tela_vendas.ui')

#Botões
pushMenu = inicio.pushMenu.clicked.connect(function_menu)
pushVendas = inicio.pushVendas.clicked.connect(vendas)
pushEstoque = inicio.pushEstoque.clicked.connect(estoque)
pushVoltar = tela_estoque.pushVoltar.clicked.connect(tela_inicio)
pushVoltar = tela_vendas.pushVoltar.clicked.connect(tela_inicio)
pushPesquisa


inicio.widgetMenu.hide()
inicio.show()
app.exec_()