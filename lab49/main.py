import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from form import FormWindow

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
		# tightly-coupled approach: we must know form's implementation
		self.form = FormWindow( self.label.text() )
		self.form.submit.connect(self.on_form_text_changed)
		self.form.show()

	@qtc.pyqtSlot(str)
	def on_form_text_changed(self,msg):
		self.label.setText(msg)
		self.form.close()


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())