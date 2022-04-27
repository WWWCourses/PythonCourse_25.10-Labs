from re import L
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from demoApp.ui.loginForm import LoginForm

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Demo App')

		# create widgets
		btnRegistration = qtw.QPushButton('Registration')
		btnLogIn = qtw.QPushButton('LogIn')
		self.le = qtw.QLineEdit(parent=self)
		self.le.setGeometry(10, 100, 100, 30)


		# create main layout
		main_layout = qtw.QHBoxLayout(self)
		main_layout.addWidget(btnRegistration)
		main_layout.addWidget(btnLogIn)

		# self.addWidget(le)

		btnLogIn.clicked.connect( self.onBtnLogInClick )
		self.le.editingFinished.connect(self.onLineEditManipulation)
		# le.textChanged.connect(self.onLineEditManipulation)
		self.le.textEdited.connect(self.onLineEditManipulation)
		# le.setText('Default')

		# on btnRegistration click => set 'Regstration' text to le:
		btnRegistration.clicked.connect( lambda:self.le.setText('Regstration') )

		self.show()

	def onBtnLogInClick(self, *args):
		print(args)
		print('btnLogIn was clicked')

		# self.form  = LoginForm()
		# self.form.show()

	def onLineEditManipulation(self,text):
		print(text)
		print('onLineEditManipulation')


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv)

	window = MainWindow()

	sys.exit(app.exec_())
