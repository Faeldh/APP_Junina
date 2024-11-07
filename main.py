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

#tela inicial
inicio = uic.loadUi("telas/tela_inicial.ui")


inicio.show()
app.exec_()