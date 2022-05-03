import sys
from PyQt5 import QtWidgets as qtw
from SimpleLoginForm.loginForm import LoginForm

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('Simple User Managment')

		# create widgets
		btnRegistration = qtw.QPushButton('Registration')
		btnLogIn = qtw.QPushButton('LogIn')

		# create main layout
		main_layout = qtw.QHBoxLayout(self)
		main_layout.addWidget(btnRegistration)
		main_layout.addWidget(btnLogIn)

		# signals:
		btnLogIn.clicked.connect( self.onBtnLogInClick )
		btnRegistration.clicked.connect( self.onBtnRegistrationClick )

	def onBtnLogInClick(self):
		self.loginForm = LoginForm()
		self.loginForm.show()

	def onBtnRegistrationClick(self):
		print('Registration Form should be shown')

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  main = MainWindow()
  main.show()

  sys.exit(app.exec())