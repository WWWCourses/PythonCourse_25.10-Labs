import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')

		btn1 = qtw.QPushButton('OK')
		btn2 = qtw.QPushButton('OK')

		ml=qtw.QHBoxLayout()
		ml.addWidget(btn1)
		ml.addWidget(btn2)

		self.setLayout(ml)

		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
