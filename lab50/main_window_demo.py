import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.setGeometry(200,200,600,600)

		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)

		self.add_menubar()
		self.add_toolbar()
		self.add_statusbar()

		self.show()

	def add_menubar(self):
		# get the menu bar
		menubar = self.menuBar()

		# add menu items
		file_menu = menubar.addMenu('&File')
		edit_menu = menubar.addMenu('Edi&t')
		help_menu = menubar.addMenu('He&lp')

		# add actions
		open_action = file_menu.addAction('Open')
		save_action = file_menu.addAction('Save')

		# add separator
		file_menu.addSeparator()

		quit_action = file_menu.addAction('Quit', self.close)
		undo_action = edit_menu.addAction('Undo', self.textedit.undo)

		# create a QAction manually
		redo_action = qtw.QAction('Redo', self)
		redo_action.triggered.connect(self.textedit.redo)

		# Actions, which opens custom dialog
		edit_menu.addAction(redo_action)
		# edit_menu.addAction('Set Font…', self.set_font)
		# edit_menu.addAction('Settings…', self.show_settings)

	def add_toolbar(self):
		toolbar = self.addToolBar('File')

		toolbar.setMovable(True)
		toolbar.setFloatable(True)
		toolbar.setAllowedAreas(
			qtc.Qt.TopToolBarArea |
			qtc.Qt.BottomToolBarArea |
			qtc.Qt.LeftToolBarArea
		)

		help_action = qtw.QAction(
			self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton),
			'Help',
			self,  # important to pass the parent!
			# add signal
			triggered=lambda: self.StatusBar().showMessage(
					'Sorry, no help yet!'
			)
		)
		toolbar.addAction(help_action)

	def add_statusbar(self):
		s = qtw.QStatusBar(self)
		self.setStatusBar(s)
		s.showMessage('Welcome to My Text Editor')

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
