# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalWordle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 750)
        MainWindow.setMinimumSize(QtCore.QSize(420, 750))
        MainWindow.setMaximumSize(QtCore.QSize(420, 750))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"font: 75 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 650, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 75 20pt \"Arial\";\n"
"background-color: rgb(52, 52, 52);")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 331, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Main_Label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Main_Label.setFont(font)
        self.Main_Label.setStyleSheet("font: 75 8pt \"Palatino Linotype\";\n"
"color: rgb(255, 255, 255);")
        self.Main_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_Label.setObjectName("Main_Label")
        self.verticalLayout.addWidget(self.Main_Label)
        self.Main_Label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Main_Label_2.setFont(font)
        self.Main_Label_2.setStyleSheet("font: 75 8pt \"Palatino Linotype\";\n"
"color: rgb(255, 255, 255);")
        self.Main_Label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_Label_2.setObjectName("Main_Label_2")
        self.verticalLayout.addWidget(self.Main_Label_2)
        self.Row1 = QtWidgets.QHBoxLayout()
        self.Row1.setObjectName("Row1")
        self.R1C1 = QtWidgets.QLabel(self.layoutWidget)
        self.R1C1.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R1C1.setAlignment(QtCore.Qt.AlignCenter)
        self.R1C1.setObjectName("R1C1")
        self.Row1.addWidget(self.R1C1)
        self.R1C2 = QtWidgets.QLabel(self.layoutWidget)
        self.R1C2.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R1C2.setAlignment(QtCore.Qt.AlignCenter)
        self.R1C2.setObjectName("R1C2")
        self.Row1.addWidget(self.R1C2)
        self.R1C3 = QtWidgets.QLabel(self.layoutWidget)
        self.R1C3.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R1C3.setAlignment(QtCore.Qt.AlignCenter)
        self.R1C3.setObjectName("R1C3")
        self.Row1.addWidget(self.R1C3)
        self.R1C4 = QtWidgets.QLabel(self.layoutWidget)
        self.R1C4.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R1C4.setAlignment(QtCore.Qt.AlignCenter)
        self.R1C4.setObjectName("R1C4")
        self.Row1.addWidget(self.R1C4)
        self.R1C5 = QtWidgets.QLabel(self.layoutWidget)
        self.R1C5.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R1C5.setAlignment(QtCore.Qt.AlignCenter)
        self.R1C5.setObjectName("R1C5")
        self.Row1.addWidget(self.R1C5)
        self.verticalLayout.addLayout(self.Row1)
        self.Row2 = QtWidgets.QHBoxLayout()
        self.Row2.setObjectName("Row2")
        self.R2C1 = QtWidgets.QLabel(self.layoutWidget)
        self.R2C1.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R2C1.setAlignment(QtCore.Qt.AlignCenter)
        self.R2C1.setObjectName("R2C1")
        self.Row2.addWidget(self.R2C1)
        self.R2C2 = QtWidgets.QLabel(self.layoutWidget)
        self.R2C2.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R2C2.setAlignment(QtCore.Qt.AlignCenter)
        self.R2C2.setObjectName("R2C2")
        self.Row2.addWidget(self.R2C2)
        self.R2C3 = QtWidgets.QLabel(self.layoutWidget)
        self.R2C3.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R2C3.setAlignment(QtCore.Qt.AlignCenter)
        self.R2C3.setObjectName("R2C3")
        self.Row2.addWidget(self.R2C3)
        self.R2C4 = QtWidgets.QLabel(self.layoutWidget)
        self.R2C4.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R2C4.setAlignment(QtCore.Qt.AlignCenter)
        self.R2C4.setObjectName("R2C4")
        self.Row2.addWidget(self.R2C4)
        self.R2C5 = QtWidgets.QLabel(self.layoutWidget)
        self.R2C5.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R2C5.setAlignment(QtCore.Qt.AlignCenter)
        self.R2C5.setObjectName("R2C5")
        self.Row2.addWidget(self.R2C5)
        self.verticalLayout.addLayout(self.Row2)
        self.Row3 = QtWidgets.QHBoxLayout()
        self.Row3.setObjectName("Row3")
        self.R3C1 = QtWidgets.QLabel(self.layoutWidget)
        self.R3C1.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R3C1.setAlignment(QtCore.Qt.AlignCenter)
        self.R3C1.setObjectName("R3C1")
        self.Row3.addWidget(self.R3C1)
        self.R3C2 = QtWidgets.QLabel(self.layoutWidget)
        self.R3C2.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R3C2.setAlignment(QtCore.Qt.AlignCenter)
        self.R3C2.setObjectName("R3C2")
        self.Row3.addWidget(self.R3C2)
        self.R3C3 = QtWidgets.QLabel(self.layoutWidget)
        self.R3C3.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R3C3.setAlignment(QtCore.Qt.AlignCenter)
        self.R3C3.setObjectName("R3C3")
        self.Row3.addWidget(self.R3C3)
        self.R3C4 = QtWidgets.QLabel(self.layoutWidget)
        self.R3C4.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R3C4.setAlignment(QtCore.Qt.AlignCenter)
        self.R3C4.setObjectName("R3C4")
        self.Row3.addWidget(self.R3C4)
        self.R3C5 = QtWidgets.QLabel(self.layoutWidget)
        self.R3C5.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R3C5.setAlignment(QtCore.Qt.AlignCenter)
        self.R3C5.setObjectName("R3C5")
        self.Row3.addWidget(self.R3C5)
        self.verticalLayout.addLayout(self.Row3)
        self.Row4 = QtWidgets.QHBoxLayout()
        self.Row4.setObjectName("Row4")
        self.R4C1 = QtWidgets.QLabel(self.layoutWidget)
        self.R4C1.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R4C1.setAlignment(QtCore.Qt.AlignCenter)
        self.R4C1.setObjectName("R4C1")
        self.Row4.addWidget(self.R4C1)
        self.R4C2 = QtWidgets.QLabel(self.layoutWidget)
        self.R4C2.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R4C2.setAlignment(QtCore.Qt.AlignCenter)
        self.R4C2.setObjectName("R4C2")
        self.Row4.addWidget(self.R4C2)
        self.R4C3 = QtWidgets.QLabel(self.layoutWidget)
        self.R4C3.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R4C3.setAlignment(QtCore.Qt.AlignCenter)
        self.R4C3.setObjectName("R4C3")
        self.Row4.addWidget(self.R4C3)
        self.R4C4 = QtWidgets.QLabel(self.layoutWidget)
        self.R4C4.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R4C4.setAlignment(QtCore.Qt.AlignCenter)
        self.R4C4.setObjectName("R4C4")
        self.Row4.addWidget(self.R4C4)
        self.R4C5 = QtWidgets.QLabel(self.layoutWidget)
        self.R4C5.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R4C5.setAlignment(QtCore.Qt.AlignCenter)
        self.R4C5.setObjectName("R4C5")
        self.Row4.addWidget(self.R4C5)
        self.verticalLayout.addLayout(self.Row4)
        self.Row5 = QtWidgets.QHBoxLayout()
        self.Row5.setObjectName("Row5")
        self.R5C1 = QtWidgets.QLabel(self.layoutWidget)
        self.R5C1.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R5C1.setAlignment(QtCore.Qt.AlignCenter)
        self.R5C1.setObjectName("R5C1")
        self.Row5.addWidget(self.R5C1)
        self.R5C2 = QtWidgets.QLabel(self.layoutWidget)
        self.R5C2.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R5C2.setAlignment(QtCore.Qt.AlignCenter)
        self.R5C2.setObjectName("R5C2")
        self.Row5.addWidget(self.R5C2)
        self.R5C3 = QtWidgets.QLabel(self.layoutWidget)
        self.R5C3.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R5C3.setAlignment(QtCore.Qt.AlignCenter)
        self.R5C3.setObjectName("R5C3")
        self.Row5.addWidget(self.R5C3)
        self.R5C4 = QtWidgets.QLabel(self.layoutWidget)
        self.R5C4.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R5C4.setAlignment(QtCore.Qt.AlignCenter)
        self.R5C4.setObjectName("R5C4")
        self.Row5.addWidget(self.R5C4)
        self.R5C5 = QtWidgets.QLabel(self.layoutWidget)
        self.R5C5.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R5C5.setAlignment(QtCore.Qt.AlignCenter)
        self.R5C5.setObjectName("R5C5")
        self.Row5.addWidget(self.R5C5)
        self.verticalLayout.addLayout(self.Row5)
        self.Row6 = QtWidgets.QHBoxLayout()
        self.Row6.setObjectName("Row6")
        self.R6C1 = QtWidgets.QLabel(self.layoutWidget)
        self.R6C1.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R6C1.setAlignment(QtCore.Qt.AlignCenter)
        self.R6C1.setObjectName("R6C1")
        self.Row6.addWidget(self.R6C1)
        self.R6C2 = QtWidgets.QLabel(self.layoutWidget)
        self.R6C2.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R6C2.setAlignment(QtCore.Qt.AlignCenter)
        self.R6C2.setObjectName("R6C2")
        self.Row6.addWidget(self.R6C2)
        self.R6C3 = QtWidgets.QLabel(self.layoutWidget)
        self.R6C3.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R6C3.setAlignment(QtCore.Qt.AlignCenter)
        self.R6C3.setObjectName("R6C3")
        self.Row6.addWidget(self.R6C3)
        self.R6C4 = QtWidgets.QLabel(self.layoutWidget)
        self.R6C4.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R6C4.setAlignment(QtCore.Qt.AlignCenter)
        self.R6C4.setObjectName("R6C4")
        self.Row6.addWidget(self.R6C4)
        self.R6C5 = QtWidgets.QLabel(self.layoutWidget)
        self.R6C5.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.R6C5.setAlignment(QtCore.Qt.AlignCenter)
        self.R6C5.setObjectName("R6C5")
        self.Row6.addWidget(self.R6C5)
        self.verticalLayout.addLayout(self.Row6)
        self.textInput = QtWidgets.QLineEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(100, 580, 211, 51))
        self.textInput.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";")
        self.textInput.setText("")
        self.textInput.setAlignment(QtCore.Qt.AlignCenter)
        self.textInput.setObjectName("textInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 20))
        self.menubar.setObjectName("menubar")
        self.menuWorlde = QtWidgets.QMenu(self.menubar)
        self.menuWorlde.setObjectName("menuWorlde")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuWorlde.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.Main_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Wordle</span></p></body></html>"))
        self.Main_Label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R1C1.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R1C2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R1C3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R1C4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R1C5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R2C1.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R2C2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R2C3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R2C4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R2C5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R3C1.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R3C2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R3C3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R3C4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R3C5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R4C1.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R4C2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R4C3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R4C4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R4C5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R5C1.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R5C2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R5C3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R5C4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R5C5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R6C1.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R6C2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R6C3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R6C4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.R6C5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menuWorlde.setTitle(_translate("MainWindow", "Worlde"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())