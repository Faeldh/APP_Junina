# import mysql.connector
# from mysql.connector import Error
# from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage, QTimeEdit
# import sys
# from PyQt5 import uic, QtWidgets, QtCore, QtGui
# import threading
# from datetime import datetime
# import time
# import mysql
# from PyQt5.QtCore import QTimer
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from tkinter import *
# from PyQt5.uic import loadUi
# from sqlite3 import Cursor
# from PyQt5.QtCore import QTimer, QTime

import sys #
import time #
import threading #
from datetime import datetime #
from tkinter import * #
from sqlite3 import Cursor #

import mysql.connector #
from PyQt5 import uic, QtWidgets, QtCore, QtGui #
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage, QTimeEdit #
import mysql #
from PyQt5.QtCore import QTimer, QTime #
from PyQt5.uic import loadUi #
from mysql.connector import Error #
from PyQt5.QtWidgets import QApplication, QMainWindow #
from PyQt5.QtCore import QTimer #

try:
    banco = mysql.connector.connect(
        host='localhost',
        port='3307',
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
