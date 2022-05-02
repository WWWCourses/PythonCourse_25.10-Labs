import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class FormWindow(qtw.QWidget):
	# cretate custom signal which will cary a string data type data:
	submit = qtc.pyqtSignal(str);

	def __init__(self , msg, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My Form')

		# ------------------------- create and atach widgets ------------------------- #
		self.edit = qtw.QLineEdit(msg)
		self.btn_submit = qtw.QPushButton('Submit')

		self.setLayout(qtw.QVBoxLayout())
		self.layout().addWidget(self.edit)
		self.layout().addWidget(self.btn_submit)


		# ---------------------------------- signals --------------------------------- #
		self.btn_submit.clicked.connect(self.onSubmit)


	@qtc.pyqtSlot(bool)
	def onSubmit(self):
		self.submit.emit(self.edit.text())
		self.close()

class MainWindow(qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My App')

		# ------------------------- create and atach widgets ------------------------- #
		self.label = qtw.QLabel('Initial Text')
		self.btn_change = qtw.QPushButton('change text')

		self.main_layout = qtw.QVBoxLayout()
		self.main_layout.addWidget(self.label)
		self.main_layout.addWidget(self.btn_change)
		self.setLayout(self.main_layout)

		# ---------------------------------- signals --------------------------------- #
		self.btn_change.clicked.connect(self.onChangeClicked)

		self.show()

	def onChangeClicked(self):
		# loosly-coupled approach: we don't care about form's implementation, just pass and receive data
		self.form = FormWindow(self.label.text())
		self.form.submit.connect(self.label.setText)
		self.form.show()


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())