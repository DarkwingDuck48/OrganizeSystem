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


        hbox = QtWidgets.QHBoxLayout()
        self.centWidget.setLayout(hbox)

        self.login = QtWidgets.QLineEdit('Login')
        self.password = QtWidgets.QLineEdit('Password')

        hbox.addStretch(1)
        hbox.addWidget(self.login)
        hbox.addWidget(self.password)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())