from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class LoginForm(qtw.QWidget ):
	def __init__(self , *args, **kwargs):
		print(kwargs)
		super().__init__(*args, **kwargs)

		# --------------------------- your code starts here -------------------------- #
		# create user input widgets:
		user_name_input = qtw.QLineEdit()
		password_input = qtw.QLineEdit()
		password_input.setEchoMode(qtw.QLineEdit.Password)
		# create the submit button:
		btn_submit = qtw.QPushButton('Login')
		# create title label:
		title = qtw.QLabel('Simple Login Form', parent=self)

		# create Form Layout and layout widgets in it
		form_layout = qtw.QFormLayout()
		form_layout.addRow('User name: ', user_name_input)
		form_layout.addRow('Password: ', password_input)
		form_layout.addRow('',btn_submit)

		# create  the main_layout
		main_layout = qtw.QVBoxLayout()
		main_layout.addWidget(title)
		main_layout.addLayout(form_layout)

		self.setLayout(main_layout)
		self.setWindowTitle('Simple Login Form')
		# ---------------------------- your code ends here --------------------------- #


