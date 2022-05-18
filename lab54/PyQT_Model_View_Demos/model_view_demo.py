import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtSql as qtsql
import csv

class CarParts(qtw.QWidget):
	def __init__(self):
		super().__init__()

		# self.setup_model_from_csv()
		self.setup_model_from_sqltable()
		self.setup_view()
		self.setupUI()

	def setupUI(self):
		label = qtw.QLabel('test',parent=self)

		self.main_layout = qtw.QVBoxLayout(self)
		self.main_layout.addWidget(label)
		self.main_layout.addWidget(self.table_view)

		# adjust TableView to fit its content
		self.table_view.setSizeAdjustPolicy(
        qtw.QAbstractScrollArea.AdjustToContents)

		# adjust widget to fit its content
		self.adjustSize()

	def setup_model_from_csv(self):
		header,data = self.load_data_from_csv('./data.csv')

		# initialize the model
		self.model = qtg.QStandardItemModel()

		self.model.setHorizontalHeaderLabels(header)

		for i, row in enumerate(data):
				items = [qtg.QStandardItem(item) for item in row]
				self.model.insertRow(i, items)

	def setup_model_from_sqltable(self):
		### create connnection
		con = qtsql.QSqlDatabase.addDatabase("QSQLITE")
		con.setDatabaseName("./carparts.db")
		if not con.open():
			qtw.QMessageBox.critical(
				None,
				"QTableView Example - Error!",
				"Database Error: %s" % con.lastError().databaseText(),
			)

		self.model = qtsql.QSqlTableModel(self)
		self.model.setTable("carparts")
		self.model.setEditStrategy(qtsql.QSqlTableModel.OnFieldChange)
		self.model.setHeaderData(0, qtc.Qt.Horizontal, "ID")
		self.model.setHeaderData(1, qtc.Qt.Horizontal, "Name")
		self.model.setHeaderData(2, qtc.Qt.Horizontal, "Category")
		self.model.setHeaderData(3, qtc.Qt.Horizontal, "Price")
		self.model.select()

	def setup_view(self):
		# setup table view
		table_view = qtw.QTableView()
		table_view.SelectionMode(3)

		# set up the view to display items in the model
		table_view.setModel(self.model)
		self.table_view = table_view

	def load_data_from_csv(self,filename):
		header = list()
		data = list()
		with open(filename,'r') as f:
			r = csv.reader(f,delimiter=';')

			header = next(r)
			for line in r:
				data.append(line)

		return (header,data)

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.carparts = CarParts()
		self.carparts.setParent(self)
		# self.carparts.show()

		self.show()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())