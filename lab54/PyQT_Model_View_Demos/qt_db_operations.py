import sys
from PyQt5 import QtSql as qtsql

class CarPartsDB:
	def __init__(self):
		# Create connection to database. If db file does not exist,
		# a new db file will be created.
		database = qtsql.QSqlDatabase.addDatabase("QSQLITE")
		database.setDatabaseName("./carparts.db")
		if not database.open():
			print("Unable to open data source file.")
			sys.exit(1) # Error code 1 - signifies error

	def createTable(self):
		query = qtsql.QSqlQuery()

		# delete carparts table if exists:
		query.exec('DROP TABLE IF EXISTS carparts')

		# create carparts table:
		query.prepare("""
			CREATE TABLE IF NOT EXISTS carparts (
				id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
				name VARCHAR(30) NOT NULL,
				category VARCHAR(30) NOT NULL,
				price REAL NOT NULL
			)
		""")
		if not query.exec():
			print('Create Table Error:', query.lastError().text())
			exit(1)
		else:
			print("[INFO] Database successfully created.")

	def insertData(self):
		query = qtsql.QSqlQuery()

		# Positional binding to insert records into the database
		query.prepare("""
			INSERT INTO carparts (name, category,price) VALUES (?, ?, ?)
		""")

		data = [
			["Part1","categoryA",1.23],
			["Part2","categoryA",1.43],
			["Part3","categoryB",4.65],
			["Part4","categoryB",2.65],
		]

		for row in data:
			query.addBindValue(row[0])
			query.addBindValue(row[1])
			query.addBindValue(row[2])
			query.exec()

if __name__=='__main__':
	db = CarPartsDB()
	db.createTable()
	db.insertData()
