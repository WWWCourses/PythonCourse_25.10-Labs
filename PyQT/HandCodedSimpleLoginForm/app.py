import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QMainWindow ):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		# main_label = qtw.QLabel('Simple Login Form', parent=self)

		form_layout = qtw.QFormLayout()

		lblUserName = qtw.QLabel('User Name')
		lblPass = qtw.QLabel('Password')
		leUserName = qtw.QLineEdit()
		lePass = qtw.QLineEdit()

		form_layout.addWidget(lblUserName)
		form_layout.addWidget(lblPass)
		form_layout.addWidget(leUserName)
		form_layout.addWidget(lePass)

		self.setLayout(form_layout)

		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	# window = MainWindow(cursor=qtc.Qt.WaitCursor,windowTitle="THIS IS MY APP")
	window = MainWindow()
	window.setWindowTitle('Simple Login Form')
	# window.setCursor(qtc.Qt.WaitCursor)

	window.setGeometry(0, 0, 800, 400)

	sys.exit(app.exec_())
