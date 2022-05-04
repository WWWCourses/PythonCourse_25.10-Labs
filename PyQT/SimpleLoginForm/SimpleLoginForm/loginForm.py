from cgitb import text
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


if __name__ == '__main__':
	from Ui_form import Ui_Form
	from db import DB
else:
	from SimpleLoginForm.Ui_form import Ui_Form
	from SimpleLoginForm.db import DB

class LoginForm(Ui_Form, qtw.QWidget):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setupUi(self)
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


if __name__ == '__main__':
	app = qtw.QApplication([])

	form = LoginForm()
	form.show()

	app.exec()

