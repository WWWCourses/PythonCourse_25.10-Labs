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

		# create main layout
		main_layout = qtw.QHBoxLayout(self)
		main_layout.addWidget(btnRegistration)
		main_layout.addWidget(btnLogIn)
		# main_layout.setStretch(0, 200)


		# on event fired  = > eventHandlerFunction()
		# signal emmited  => slot()
		# btnLogIn click  => onBtnLogInClick()

		### one object an have many signals
		# btnLogIn.clicked.connect( lambda : print('Click') )
		# btnLogIn.pressed.connect( lambda : print('Pressed') )
		# btnLogIn.released.connect( lambda : print('Released') )

		### One signal can be connected to one or many slots
		# btnLogIn.clicked.connect( lambda: print('Hello') )

		btnLogIn.clicked.connect( self.onBtnLogInClick )

		self.show();

	def onBtnLogInClick(self):
		print('btnLogIn was clicked')
		self.loginForm = LoginForm()
		self.loginForm.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
