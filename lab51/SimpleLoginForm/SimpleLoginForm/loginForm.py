from cgitb import text
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import os


if __name__ == '__main__':
	from Ui_form import Ui_Form
	from db import DB
	filename = './form_style.css'
else:
	from SimpleLoginForm.Ui_form import Ui_Form
	from SimpleLoginForm.db import DB
	filename = './SimpleLoginForm/form_style.css'


class LoginForm(Ui_Form, qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		print(f'CWD: {os.getcwd()}')

		self.setupUi(self)
		# style widgets
		# self.labelUsername.setStyleSheet('color:#F00;background-color:#999')
		# load style sheet in external css file:
		self.main_style = self.load_style_sheet()
		self.setStyleSheet(self.main_style)


		self.btnSubmit.clicked.connect( self.onBtnSubmitClick )
		self.btnCancel.clicked.connect(self.close)

		self.db = DB('test', 'test1234','test')

	@qtc.pyqtSlot(bool)
	def onBtnSubmitClick(self):
		user_name = self.leUserName.text()
		user_pasword = self.lePass.text()
		print(user_name, user_pasword)

		# HW: add your code, which will check if user exists in DB
		if self.db.authenticate(user_name=user_name, password=user_pasword):
			self.handleLoginSuccess()
		else:
			self.handleLoginFail()

	def handleLoginSuccess(self):
		msg_box = qtw.QMessageBox()
		msg_box.setIcon(qtw.QMessageBox.Information)
		msg_box.setText("User is successfuly loged in!")
		msg_box.setInformativeText("Some informative text")
		msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
		msg_box.setDefaultButton(qtw.QMessageBox.Ok)
		msg_box.exec();

	def handleLoginFail(self):
		msg_box = qtw.QMessageBox()
		msg_box.setIcon(qtw.QMessageBox.Critical)
		msg_box.setText("User is not loged in")
		# msg_box.setInformativeText("Some informative text");
		msg_box.setStandardButtons(qtw.QMessageBox.Ok);
		msg_box.setDefaultButton(qtw.QMessageBox.Ok);
		msg_box.buttonClicked.connect(lambda btn: print(btn.text()))
		msg_box.exec()

	def load_style_sheet(self):
		with open(filename,'r') as fh:
			return fh.read()

if __name__ == '__main__':
	app = qtw.QApplication([])

	form = LoginForm()
	form.show()

	app.exec()

