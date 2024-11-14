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
    QFileDialog, QApplication, QWidget, 
    QPushButton, QTableWidget, 
    QErrorMessage, QTimeEdit, QMainWindow
)
from PyQt5.QtCore import QTimer, QTime

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

def estoque():
    tela_estoque.show()
    tableEstoque()
    inicio.close()

def vendas():
    tela_vendas.show()
    tableLista()
    inicio.close()

def tela_inicio():
    inicio.show()
    tela_estoque.close()
    tela_vendas.close()

# def vendaPesquisa():

def tableEstoque():
    try: # Mostrar na tabela
        banco = mysql.connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = '12345678',
            database = 'appjunina'
        )
        cursor = banco.cursor()

        cursor.execute("SELECT id, nome, valor_unit, quant_total FROM estoque")
        selecao = cursor.fetchall()

        tela_estoque.tableEstoque.setRowCount(len(selecao))

        print("Início do looping")

        for i in range(len(selecao)):
            for j in range(5): # Adicionando Linhas na tabela
                if(j == 4):
                    calculo = selecao[i][2] * selecao[i][3]
                    tela_estoque.tableEstoque.setItem(i, j, QtWidgets.QTableWidgetItem(str(calculo)))
                else:
                    tela_estoque.tableEstoque.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))
        print("Final do looping")
    except:
        print("Erro na função de mostrar na tabela")
        print(f"{selecao}")
    finally:
        cursor.close()
        banco.close()

def tableLista():
    try:
        banco = mysql.connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = '12345678',
            database = 'appjunina'
        )
        cursor = banco.cursor()

        cursor.execute("SELECT id, nome, quant_total FROM estoque")
        selecao = cursor.fetchall()

        tela_vendas.tableListaEstoque.setRowCount(len(selecao))

        print("Início do looping")
        for i in range(len(selecao)):
            for j in range(3):
                tela_vendas.tableListaEstoque.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))
    except:
        print("Erro na função de mostrar tabela de vendas")
    finally:
        cursor.close()
        banco.close()

# def adicionar estoque
def adicionar_estoque():
    print("Inicío da função")
    nome = tela_estoque.lineNome.text()
    valor_unit = float(tela_estoque.lineValorUNIT.text())
    quant_total = int(tela_estoque.lineQuant.text())

    colunas = "nome, valor_unit, quant_total"

    try:
        print("Conexão com o banco de dados")
        banco = mysql.connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = '12345678',
            database = 'appjunina'
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
        print("Erro na função adicionar_estoque: ", str(e))
        erro_produto.exec_()
    finally:
        if banco.is_connected():
            tableEstoque()

def remover_estoque():
    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '12345678',
        database = 'appjunina'
    )
    cursor = banco.cursor()
    id = int(tela_estoque.lineID.text())

    try:
        print("Início da função")
        query = f"DELETE FROM estoque WHERE id = %s"
        values = (id, )
        cursor.execute(query, values)

        banco.commit()
    except mysql.connector.Error as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro ao conectar ao banco de dados: {str(e)}")
        print("Erro na função Deletar", str(e))
        erro_produto.exec_()
    finally:
        if banco.is_connected():
            tableEstoque()

def atualizar_estoque():
    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '12345678',
        database = 'appjunina'
    )
    cursor = banco.cursor()

    print("Inicio da função")
    id = int(tela_estoque.lineID.text())
    nome = tela_estoque.lineNome.text()
    valor_unit = float(tela_estoque.lineValorUNIT.text())
    quant_total = int(tela_estoque.lineQuant.text())

    try:
        print("Início da Query")
        query = f"UPDATE estoque SET nome = %s, valor_unit = %s, quant_total = %s WHERE id = %s"
        values = (nome, valor_unit, quant_total, id)
        cursor.execute(query, values)
        print("Final da Query")

        banco.commit()

    except mysql.connector.Error as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro ao conectar ao banco de dados: {str(e)}")
        print("Erro na função Atualizar", str(e))
        erro_produto.exec_()

    finally:
        if banco.is_connected():
            tableEstoque()

def pesquisa_vendas():
    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '12345678',
        database = 'appjunina'
    )
    cursor = banco.cursor()
    pesquisa = ""

    id = tela_vendas.lineID.text()
    nome = tela_vendas.lineNome.text()

    print("Inicio da função")

    if(nome != "" and id == ""): # nome preenchido / id vazio
        query = "SELECT id, nome, quant_total FROM estoque WHERE nome LIKE %s"
        values = ('%' + nome + '%', )
    elif(nome == "" and id != ""): # nome vazio / id preenchido
        id = int(tela_vendas.lineID.text())
        query = "SELECT id, nome, quant_total FROM estoque WHERE id = %s"
        values = (id, )
        pesquisa = True
    elif(nome != "" and id != ""): # nome e id preenchidos
        id = int(tela_vendas.lineID.text())
        query = "SELECT id, nome, quant_total FROM estoque WHERE id = %s OR nome LIKE %s"
        values = (id, '%' + nome + '%')
    else: # nome e id vazios
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Não possui valor na pesquisa: {str(mysql.connector.Error)}")
        print("Sem valor pra pesquisa", str(mysql.connector.Error))
        erro_produto.exec_()
        return

    cursor.execute(query, values)
    selecao = cursor.fetchall()
    
    tela_vendas.tablePesquisa.setRowCount(len(selecao))

    # Looping
    for i in range(len(selecao)):
        for j in range(3):
            tela_vendas.tablePesquisa.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))

    if(pesquisa == True):
        id = tela_vendas.lineID.text()
        query = "SELECT nome, valor_unit FROM estoque WHERE id = %s"
        values = (id, )
        cursor.execute(query, values)
        result = cursor.fetchone()
        valor_unit = float(result[1])
        nome = result[0]
        nome = tela_vendas.lineNome.setText(f"{nome}")
        valorUNIT = tela_vendas.labelValorUNIT.setText(f"{valor_unit:.2f}")

def adicionar_vendas():
    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '12345678',
        database = 'appjunina'
    )
    cursor = banco.cursor()
    
    id = tela_vendas.lineID.text()
    nome = tela_vendas.lineNome.text()
    try:
        valorUNIT = float(tela_vendas.labelValorUNIT.text())
        valorUNIT = float("{:.2f}".format(valorUNIT))  # Arredonda para duas casas decimais
        quant = int(tela_vendas.lineQuant.text())

        total = valorUNIT * quant
        total = float("{:.2f}".format(total)) # Arredonda para duas casas decimais

        colunas = "id, nome, valor_unit, quant, total"

    
        print("Início da Query")
        query = f"INSERT INTO vendas ({colunas}) VALUES (%s, %s, %s, %s, %s)"
        values = (id, nome, valorUNIT, quant, total)
        cursor.execute(query, values)
        print("Final da função")

        banco.commit()

    except (ValueError, TypeError) as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro de valor: {str(e)}")
        print("Erro de valor na função adicionar_vendas", str(e))
        erro_produto.exec_()

    finally:
        if banco.is_connected():
            tableVendas()

def tableVendas():
    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '12345678',
        database = 'appjunina'
    )
    print('Término do banco')
    cursor = banco.cursor()

    try:
        print("Início da Query")
        cursor.execute("SELECT id, nome, valor_unit, quant, total FROM vendas")
        result = cursor.fetchall()
        linha = len(result)
        tela_vendas.tableVendas.setRowCount(linha) # Sempre conferir a quantidade de linhas com "setRowCount"

        print('Inicio do looping TableVendas')
        for i in range(linha):
            for j in range(5):
                tela_vendas.tableVendas.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
        print("Final do Looping tableVendas")
    except mysql.connector.Error as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro na função tableVendas {str(e)}")
        print("Erro na função tableVendas", str(e))
        erro_produto.exec_()
    finally:
        total_vendas()

def remover_vendas():
    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '12345678',
        database = 'appjunina'
    )
    cursor = banco.cursor()

    try:
        id = int(tela_vendas.lineID.text())
        print("Início da função")
        query = f"DELETE FROM vendas WHERE id = %s"
        values = (id, )
        cursor.execute(query, values)

        banco.commit()

    except (ValueError, TypeError) as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro de valor: {str(e)}")
        print("Erro de valor na função remover_vendas", str(e))
        erro_produto.exec_()
    finally:
        if banco.is_connected():
            tableVendas()

def valor_total_item():
    try:
        valorUNIT = float(tela_vendas.labelValorUNIT.text())
        quant = int(tela_vendas.lineQuant.text())

        soma = valorUNIT * quant
        valorTotal = tela_vendas.labelValorTotalItem.setText(f"{soma}")
    except (ValueError, TypeError) as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro de valor: {str(e)}")
        print("Erro de valor na função valor_total_item:", str(e))
        erro_produto.exec_()
    finally:
        print("Final da função valor_total_item")

def total_vendas():
    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '12345678',
        database = 'appjunina'
    )
    print('Inicio total vendas')
    cursor = banco.cursor()
    
    try:
        print('inicio da query')
        query = 'SELECT SUM(total) from vendas'
        cursor.execute(query, )

        tot = cursor.fetchone()[0]

        labelValorTotal = tela_vendas.labelValorTotal.setText(f'{tot:.2f}')
        print('Fim da função')
    except mysql.connector.Error as e:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage(f"Erro na função total_vendas {str(e)}")
        print("Erro na função total_vendas", str(e))
        erro_produto.exec_()

# tela inicial
inicio = uic.loadUi('telas/tela_menu.ui')
tela_estoque = uic.loadUi('telas/tela_estoque.ui')
tela_vendas = uic.loadUi('telas/tela_vendas.ui')

#Campos das tela
tela_vendas.lineQuant.editingFinished.connect(valor_total_item)

# Botões - Telas
pushMenu = inicio.pushMenu.clicked.connect(function_menu)
pushVendas = inicio.pushVendas.clicked.connect(vendas)
pushEstoque = inicio.pushEstoque.clicked.connect(estoque)

# Botões - Voltar
pushVoltar = tela_estoque.pushVoltar.clicked.connect(tela_inicio)
pushVoltar = tela_vendas.pushVoltar.clicked.connect(tela_inicio)

# Botões Vendas
pushPesquisaVendas = tela_vendas.pushPesquisa.clicked.connect(pesquisa_vendas)
pushAdicionarVendas = tela_vendas.pushAdicionar.clicked.connect(adicionar_vendas)
pushRemoverVendas = tela_vendas.pushRemover.clicked.connect(remover_vendas)

# Botões Estoque
pushAdicionarEstoque = tela_estoque.pushAdicionar.clicked.connect(adicionar_estoque)
pushAtualizarEstoque = tela_estoque.pushAtualizar.clicked.connect(atualizar_estoque)
pushRemoverEstoque = tela_estoque.pushRemover.clicked.connect(remover_estoque)

inicio.widgetMenu.hide()
inicio.show()
app.exec_()