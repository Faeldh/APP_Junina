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

banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = '12345678',
    database = 'appjunina'
)

try:
    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='12345678',
        database='appjunina'
    )
    cursor = banco.cursor()
    if banco.is_connected():
        print("Conexão bem-sucedida!")
except mysql.connector.Error as e:
    print(f"Erro ao conectar: {e}")
finally:
    if banco.is_connected():
        banco.close()
