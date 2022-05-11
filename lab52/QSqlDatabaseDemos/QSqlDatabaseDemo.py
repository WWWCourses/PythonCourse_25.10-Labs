import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from db import DB

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')

		self.btnLogin = qtw.QPushButton('Login')
		self.main_layout = qtw.QVBoxLayout(self)
		self.main_layout.addWidget(self.btnLogin)

		self.btnLogin.clicked.connect(self.btnLoginHandler)

		db = DB()


		self.show();

	def btnLoginHandler(self):
		print('btnLoginHandler called')




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
