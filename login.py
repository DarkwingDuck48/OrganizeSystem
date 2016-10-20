import sys
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Login')

        self.show()

        self.centWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centWidget)

        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        hbox_2 = QtWidgets.QHBoxLayout()

        self.centWidget.setLayout(vbox)

        self.login = QtWidgets.QLineEdit('Login')
        self.password = QtWidgets.QLineEdit('Password')
        self.btn_start = QtWidgets.QPushButton('Log in')

        hbox.addStretch(1)
        hbox.addWidget(self.login)
        hbox.addWidget(self.password)

        vbox.addLayout(hbox)
        hbox_2.addSpacing(20)
        hbox_2.addWidget(self.btn_start)
        hbox_2.addSpacing(20)
        vbox.addLayout(hbox_2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())