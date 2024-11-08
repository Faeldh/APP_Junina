# Imports de módulos padrão
import sys
import time
import threading
from datetime import datetime
from tkinter import *
from sqlite3 import Cursor

# Imports de terceiros
import mysql.connector
from mysql.connector import Error
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, 
    QErrorMessage, QTimeEdit, QMainWindow
)
from PyQt5.QtCore import QTimer, QTime

app = QtWidgets.QApplication([])

banco = mysql.connector.connect(
    host = 'localhost',
    port = '3307',
    user = 'root',
    password = '12345678',
    database = 'appjunina'
)

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

# def vendaPesquisa():

# def adicionar estoque
def adicionar_estoque():
    print("Inicío da função")
    nome = tela_estoque.lineNome.text()
    valor_unit = tela_estoque.lineValorUNIT.text()
    valor_unit = float(valor_unit)
    quant_total = tela_estoque.lineQuant.text()
    quant_total = int(quant_total)

    colunas = f"nome, valor_unit, quant_total"

    try:
        print("Conexão com o banco de dados")
        banco = mysql.connector.connect(
            host='localhost',
            port='3307',
            user='root',
            password='12345678',
            database='appjunina'
        )
        cursor = banco.cursor()

        print("Início da Query")
        query = f"INSERT INTO estoque ({colunas}) VALUES (%s, %s, %s)"
        values = (nome, valor_unit, quant_total)
        cursor.execute(query, values)
        print("Final da função")

        banco.commit()
    except mysql.connector.Error as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro ao conectar ao banco de dados: {str(e)}")
        print("Erro na conexão ou execução do SQL: ", str(e))
        erro_produto.exec_()
    finally:
        if banco.is_connected():
            cursor.close()
            banco.close()


# tela inicial
inicio = uic.loadUi('telas/tela_menu.ui')
tela_estoque = uic.loadUi('telas/tela_estoque.ui')
tela_vendas = uic.loadUi('telas/tela_vendas.ui')

# Botões - Telas
pushMenu = inicio.pushMenu.clicked.connect(function_menu)
pushVendas = inicio.pushVendas.clicked.connect(vendas)
pushEstoque = inicio.pushEstoque.clicked.connect(estoque)

# Botões - Voltar
pushVoltar = tela_estoque.pushVoltar.clicked.connect(tela_inicio)
pushVoltar = tela_vendas.pushVoltar.clicked.connect(tela_inicio)

# Pesquisa
#pushPesquisar = tela_vendas.pushPesquisar.clicked.connect()

#Adicionar
#pushAdicionar = tela_vendas.pushAdicionar.clicked.connect()
pushAdicionarEstoque = tela_estoque.pushAdicionar.clicked.connect(adicionar_estoque)

inicio.widgetMenu.hide()
inicio.show()
app.exec_()