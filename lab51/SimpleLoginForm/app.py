import sys
from PyQt5 import QtWidgets as qtw
from SimpleLoginForm.loginForm import LoginForm

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('Simple User Managment')
		self.form = LoginForm(parent=self)




if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  main = MainWindow()
  main.show()

  sys.exit(app.exec())