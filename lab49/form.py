from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# self.form = FormWindow( 'some text')

class FormWindow(qtw.QWidget):
	# cretate custom signal which will cary a string data type data:
	submit = qtc.pyqtSignal(str)

	def __init__(self , msg, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My Form')

		# ------------------------- create and atach widgets ------------------------- #
		self.edit = qtw.QLineEdit()
		self.edit.setText( msg )
		self.btn_submit = qtw.QPushButton('Submit')

		self.setLayout(qtw.QVBoxLayout())
		self.layout().addWidget(self.edit)
		self.layout().addWidget(self.btn_submit)


		self.btn_submit.clicked.connect(lambda : self.submit.emit(self.edit.text()))

