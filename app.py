from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QTabWidget, QLineEdit)
from PyQt5.QtGui import QFont
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Methods of search engine optimization")
        self.setFixedSize(QSize(1366, 768))

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.lab1 = QWidget()
        self.lab2 = QWidget()
        self.tabs.resize(300,200)

        self.tabs.addTab(self.lab1, "Lab 1")
        self.tabs.addTab(self.lab2, "Lab 2")

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111, projection='3d')

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.lab1.layout1 = QVBoxLayout(self)
        self.lab1.layout2 = QVBoxLayout(self)
        self.lab1.layout = QHBoxLayout(self)
        self.lab1.layout.addLayout(self.lab1.layout1, 70)
        self.lab1.layout.addLayout(self.lab1.layout2, 30)

        self.lab1.layout1.addWidget(self.toolbar)
        self.lab1.layout1.addWidget(self.canvas)

        self.lab1.layout3 = QHBoxLayout(self)
        self.lab1.layout4 = QHBoxLayout(self)
        self.lab1.layout5 = QHBoxLayout(self)
        self.lab1.layout6 = QHBoxLayout(self)
        self.lab1.layout7 = QHBoxLayout(self)
        self.lab1.layout8 = QHBoxLayout(self)
        self.lab1.layout9 = QHBoxLayout(self)
        self.lab1.layout10 = QHBoxLayout(self)
        self.lab1.layoutP = QHBoxLayout(self)
        self.lab1.layout2.addLayout(self.lab1.layout3, 10)
        self.lab1.layout2.addLayout(self.lab1.layout4, 10)
        self.lab1.layout2.addLayout(self.lab1.layout5, 10)
        self.lab1.layout2.addLayout(self.lab1.layout6, 10)
        self.lab1.layout2.addLayout(self.lab1.layout7, 10)
        self.lab1.layout2.addLayout(self.lab1.layout8, 10)
        self.lab1.layout2.addLayout(self.lab1.layoutP, 5)
        self.lab1.layout2.addLayout(self.lab1.layout9)
        self.lab1.layout2.addLayout(self.lab1.layout10, 30)

        self.text1 = QLabel("Начальная точка Х:", self)
        self.lab1.layout3.addWidget(self.text1)
        self.text1.setFont(QFont("Gilroy bold", 16))
        self.lab1.layout3.addStretch()
        self.text1v = QLineEdit(self)
        self.text1v.setAlignment(Qt.AlignCenter)
        self.lab1.layout3.addWidget(self.text1v)
        self.lab1.layout3.addStretch()

        self.text2 = QLabel("Начальная точка У:", self)
        self.lab1.layout4.addWidget(self.text2)
        self.text2.setFont(QFont("Gilroy bold", 16))
        self.lab1.layout4.addStretch()
        self.text2v = QLineEdit(self)
        self.text2v.setAlignment(Qt.AlignCenter)
        self.lab1.layout4.addWidget(self.text2v)
        self.lab1.layout4.addStretch()

        self.text3 = QLabel("Начальный шаг:    ", self)
        self.lab1.layout5.addWidget(self.text3)
        self.text3.setFont(QFont("Gilroy bold", 16))
        self.lab1.layout5.addStretch()
        self.text3v = QLineEdit(self)
        self.lab1.layout5.addWidget(self.text3v)
        self.lab1.layout5.addStretch()

        self.text4 = QLabel("Число итераций:   ", self)
        self.lab1.layout6.addWidget(self.text4)
        self.text4.setFont(QFont("Gilroy bold", 16))
        self.lab1.layout6.addStretch()
        self.text3v = QLineEdit(self)
        self.lab1.layout6.addWidget(self.text3v)
        self.lab1.layout6.addStretch()

        self.text5 = QLabel("Задержка:            ", self)
        self.lab1.layout7.addWidget(self.text5)
        self.text5.setFont(QFont("Gilroy bold", 16))
        self.lab1.layout7.addStretch()
        self.text3v = QLineEdit(self)
        self.lab1.layout7.addWidget(self.text3v)
        self.lab1.layout7.addStretch()

        self.okButton = QPushButton("Выполнить", self)
        self.okButton.setFont(QFont("Gilroy bold", 16))
        self.lab1.layout8.addWidget(self.okButton)

        self.text6 = QLabel("Выполнение и результаты", self)
        self.lab1.layout9.addWidget(self.text6)
        self.text6.setFont(QFont("Gilroy bold", 12))

        self.infoLabel = QLabel(self)
        self.infoLabel.setFont(QFont("Gilroy bold", 16))
        self.infoLabel.setStyleSheet("QLabel { border: 1px solid black; }") 
        self.lab1.layout10.addWidget(self.infoLabel)  

        # График функции Химмельблау
        X = np.arange(-6, 6, 0.1)
        Y = np.arange(-6, 6, 0.1)
        X, Y = np.meshgrid(X, Y)
        Z = (X * X + Y - 11) ** 2 + (X + Y * Y - 7) ** 2

        self.axes.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='plasma')

        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Y')
        self.axes.set_zlabel('Z')
        self.axes.tick_params(axis='x', labelsize=6)  # Уменьшаем размер меток по оси X
        self.axes.tick_params(axis='y', labelsize=6)  # Уменьшаем размер меток по оси Y
        self.axes.tick_params(axis='z', labelsize=6)  # Уменьшаем размер меток по оси Z

        self.lab1.setLayout(self.lab1.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Widget()
    i = QtGui.QIcon("icon.png")
    win.setWindowIcon(i)
    app.setWindowIcon(i)
    win.show()
    sys.exit(app.exec_())
