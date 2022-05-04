import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.main_layout = qtw.QVBoxLayout(self)

		self.title = qtw.QLabel('Welcome to my App1', parent=self)
		self.copyright = qtw.QLabel('2022',parent=self)
		self.btn = qtw.QPushButton('OK')

		self.main_layout.addWidget(self.title)
		self.main_layout.addWidget(self.copyright)
		self.main_layout.addWidget(self.btn)


		# style labels:
		self.main_style = self.read_style()

		#widgetInstance.setStyleSheet(sheet)
		self.setStyleSheet(self.main_style)




		self.show();

	def read_style(self):
		with open("styles.css", 'r') as fh:
			sheet = fh.read()
			return sheet





if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
