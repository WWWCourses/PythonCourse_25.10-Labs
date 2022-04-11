import mysql.connector
from mysql.connector import connection

def make_connection(user, password, db, host="localhost", port=3306):
	try:
		cnx = mysql.connector.connect(
			user=user,
			password=password,
			db=db,
			host=host,
			port=port
		)

	except mysql.connector.Error as e:
		print(e)

	print('Connection Established')
	return cnx



# Connect to server
cnx = make_connection (user="test", password="test1234", db='test')

# Get a cursor
# cur = cnx.cursor()

# # Execute a query
# cur.execute("SELECT CURDATE()")

# row = cur.fetchone()
# print(row)


# cur.execute("""SELECT t1.first_name,t2.order_date FROM customers t1
# 	INNER JOIN orders t2
# ON t1.id = t2.customer_id;""")


# for row in cur.fetchall():
# 	print(row)


# ------------------------------ prepared query: ----------------------------- #
user_name = 'Ada'

with cnx.cursor() as cur:
	# cur.execute(f'''SELECT order_date, customer_id
	# FROM test.orders,test.customers
	# WHERE customers.first_name='{user_name}' AND customers.id=orders.customer_id;''')

	sql = """SELECT order_date, customer_id
	FROM test.orders,test.customers
	WHERE customers.first_name=%s AND customers.id=orders.customer_id;
	"""


	cur.execute(sql, (user_name,))

	for row in cur.fetchall():
		print(row)





