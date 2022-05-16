import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import csv


class Table():
	def __init__(self):
		self.setupModelView()

	def setupModelView(self):
		self.setup_model()

		# setup table view
		table_view = qtw.QTableView()
		table_view.SelectionMode(3)


		# set up the view to display items in the model
		table_view.setModel(self.model)
		self.table_view = table_view

	def setup_model(self):
		header,data = self.load_data('./data.csv')

		# initialize the model
		self.model = qtg.QStandardItemModel()
		# Set initial row and column values
		self.model.setRowCount(3)
		self.model.setColumnCount(4)

		self.model.setHorizontalHeaderLabels(header)

		for i, row in enumerate(data):
				items = [qtg.QStandardItem(item) for item in row]
				self.model.insertRow(i, items)

	def load_data(self,filename):
		header = list()
		data = list()
		with open(filename,'r') as f:
			r = csv.reader(f,delimiter=';')

			header = next(r)
			for line in r:
				data.append(line)

		print(data)

		return (header,data)


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.table = Table()

		tableViewWidth = self.table.table_view.frameGeometry().width()
		tableViewHeight = self.table.table_view.frameGeometry().height()

		self.setFixedWidth(tableViewWidth)
		self.setFixedHeight(tableViewHeight)

		v_box = qtw.QVBoxLayout()
		v_box.addWidget(self.table.table_view)
		self.setLayout(v_box)

		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
