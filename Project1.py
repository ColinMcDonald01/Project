from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(236, 311)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_id = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(40, 40, 161, 31))
        self.input_id.setObjectName("input_id")
        self.ID = QtWidgets.QLabel(parent=self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(16, 42, 61, 31))
        self.ID.setObjectName("ID")
        self.Voting_application = QtWidgets.QLabel(parent=self.centralwidget)
        self.Voting_application.setGeometry(QtCore.QRect(70, 10, 271, 31))
        self.Voting_application.setScaledContents(False)
        self.Voting_application.setObjectName("Voting_application")
        self.candidates = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates.setGeometry(QtCore.QRect(70, 70, 181, 41))
        self.candidates.setScaledContents(False)
        self.candidates.setWordWrap(False)
        self.candidates.setObjectName("candidates")
        self.radioButton_1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(70, 110, 161, 21))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 130, 151, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 170, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 180, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 210, 181, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 236, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project1 Pyqt"))
        self.ID.setText(_translate("MainWindow", "ID"))
        self.Voting_application.setText(_translate("MainWindow", "Voting Application"))
        self.candidates.setText(_translate("MainWindow", "CANDIDATES"))
        self.radioButton_1.setText(_translate("MainWindow", "Jane"))
        self.radioButton_2.setText(_translate("MainWindow", "John"))
        self.label.setText(_translate("MainWindow", "OTHER"))
        self.pushButton.setText(_translate("MainWindow", "SUBMITE VOTE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
