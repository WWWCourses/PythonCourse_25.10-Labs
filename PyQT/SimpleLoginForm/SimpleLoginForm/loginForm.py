from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from SimpleLoginForm.Ui_form import Ui_Form

class LoginForm(Ui_Form):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setupUi(self)
		self.btnSubmit.clicked.connect( self.onBtnSubmitClick )

	@qtc.pyqtSlot(bool)
	def onBtnSubmitClick(self):
		user_name = self.leUserName.text()
		user_pasword = self.lePass.text()
		print(user_name, user_pasword)

		# HW: add your code, which will check if user exists in DB


if __name__ == '__main__':
	pass
