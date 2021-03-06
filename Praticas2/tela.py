# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\andre.junges\Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from model import Model
from tkinter import filedialog, Canvas, NW

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 245)
        self.model: Model = None
        self.photo_path = None
        #MainWindow.setWindowOpacity(-2.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label.setObjectName("label")
        self.edtImagem = QtWidgets.QLineEdit(self.centralwidget)
        self.edtImagem.setGeometry(QtCore.QRect(70, 10, 231, 20))
        self.edtImagem.setObjectName("edtImagem")
        self.btnImagem = QtWidgets.QPushButton(self.centralwidget)
        self.btnImagem.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.btnImagem.setObjectName("btnImagem")
        self.edtModel = QtWidgets.QLineEdit(self.centralwidget)
        self.edtModel.setGeometry(QtCore.QRect(70, 40, 231, 20))
        self.edtModel.setObjectName("edtModel")
        self.btnModel = QtWidgets.QPushButton(self.centralwidget)
        self.btnModel.setGeometry(QtCore.QRect(310, 40, 75, 23))
        self.btnModel.setObjectName("btnModel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.edtCalibrador = QtWidgets.QLineEdit(self.centralwidget)
        self.edtCalibrador.setGeometry(QtCore.QRect(70, 70, 231, 20))
        self.edtCalibrador.setObjectName("edtCalibrador")
        self.btnCalibrador = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalibrador.setGeometry(QtCore.QRect(310, 70, 75, 23))
        self.btnCalibrador.setObjectName("btnCalibrador")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 51, 16))
        self.label_3.setObjectName("label_3")
        self.btnExecutar = QtWidgets.QPushButton(self.centralwidget)
        self.btnExecutar.setGeometry(QtCore.QRect(150, 100, 75, 23))
        self.btnExecutar.setObjectName("btnExecutar")
        self.edtResultado = QtWidgets.QLabel(self.centralwidget)
        self.edtResultado.setGeometry(QtCore.QRect(100, 150, 191, 20))
        self.edtResultado.setText("")
        self.edtResultado.setObjectName("edtResultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Imagem"))
        self.btnImagem.setText(_translate("MainWindow", "Browse"))
        self.btnModel.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Model"))
        self.btnCalibrador.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Weights"))
        self.btnExecutar.setText(_translate("MainWindow", "Executar"))
        self.btnImagem.clicked.connect(self.loadImage)
        self.btnModel.clicked.connect(self.loadModel)
        self.btnCalibrador.clicked.connect(self.loadCalibrador)
        self.btnExecutar.clicked.connect(self.exibirResultado)

    def exibirResultado(self):
        self.predict(self.edtImagem.text())        

    def loadModel(self):
        modelPath = filedialog.askdirectory()
        self.edtModel.setText(modelPath)
        self.model = Model(modelPath)        

    def predict(self, photo_path):
        print(photo_path)
        prediction = self.model.predict_ImagemSelecionada(photo_path)
        self.edtResultado.setText(f" A imagem selecionada ??: {prediction} ")

    def ObterArquivo(self, fileType: tuple):
        return filedialog.askopenfilename(filetypes=(fileType, ('All files', '.*')))        

    def loadImage(self):
        filename = self.ObterArquivo(('png', '*.png'))
        self.edtImagem.setText(filename)

    def loadCalibrador(self):
        filename = self.ObterArquivo(('h5', '*.h5'))
        self.edtCalibrador.setText(filename)
        self.model.load_weights(filename)            
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    w = Ui_MainWindow()
    w.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())