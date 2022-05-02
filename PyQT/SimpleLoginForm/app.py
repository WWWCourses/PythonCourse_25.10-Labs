import sys
from PyQt5 import QtWidgets as qtw
from SimpleLoginForm.loginForm import LoginForm

class MainWindow(qtw.QWidget, LoginForm):
	def __init__(self):
		super().__init__()

		# add as any properties here...
		self.setWindowTitle('The title of main window')

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  main = MainWindow()
  main.show()

  sys.exit(app.exec())