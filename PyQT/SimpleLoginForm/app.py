import sys
from PyQt5 import QtWidgets as qtw
from Ui_form import Ui_Form


class MainWindow(qtw.QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# add as any properties here...
		self.setWindowTitle('The title of main window')

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  main = MainWindow()
  main.show()

  sys.exit(app.exec())