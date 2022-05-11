from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5 import QtGui

class DB:
	def __init__(self) -> None:
		self.conn()
		# self.createTable()
		# self.insert_data()
		self.select_data()

	def conn(self):
		db = QSqlDatabase.addDatabase('QSQLITE')
		db.setDatabaseName('./bnr.db')

		if not db.open():
			QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
				QtGui.qApp.tr("Unable to establish a database connection.\n"),
				QtGui.QMessageBox.Cancel)

			return False

		# self.query = QSqlQuery()
		return True

	def createTable(self):
		q = QSqlQuery()
		q.exec_(f"""
				CREATE TABLE radiotheaters(
						id int primary key,
						title varchar(20),
						content varchar(100),
						date TEXT
				)
		""")

	def insertRow(self, **kwargs):
		# Creating a query for later execution using .prepare()
		q = QSqlQuery()
		q.exec_()
		q.prepare(
			"""
			INSERT INTO radiotheaters (
											title,
											content,
											date
			)
			VALUES (?, ?, ?)
			"""
		)

		q.addBindValue(kwargs['title'])
		q.addBindValue(kwargs['content'])
		q.addBindValue(kwargs['date'])
		q.exec()

	def insert_data(self):
		# Sample data
		data = [
				("Theater1", "Content1", "2021-01-01"),
				("Theater2", "Content2", "2021-01-02"),
				("Theater3", "Content3", "2021-01-03"),
				("Theater4", "Content4", "2021-01-04"),
		]

		for title, content, date in data:
			self.insertRow(title=title, content=content, date=date)

	def select_data(self):
		q = QSqlQuery()
		sql = '''select * from radiotheaters;'''
		data = q.exec(sql)
		while q.next():
			print(q.value(0))
			print(q.value(1), q.value(2), q.value(3))