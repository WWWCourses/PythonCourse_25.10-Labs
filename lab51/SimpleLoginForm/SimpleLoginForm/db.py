import mysql.connector
# from mysql.connector import connection

class DB:
	def __init__(self,user, password, db, host="localhost", port=3306):
		try:
			self.cnx = mysql.connector.connect(
				user=user,
				password=password,
				db=db,
				host=host,
				port=port
			)
		except mysql.connector.Error as e:
			print(e)
			exit()

	def authenticate(self, user_name, password):
		# create a cursor for the connection
		c= self.cnx.cursor()

		# prepare SQL query:
		q = f"""
			SELECT * FROM users
				WHERE username=%s AND password=%s
		"""
		# execute the query
		c.execute(q,(user_name,password))

		# we are only interested if 1 or 0 rows are returned
		res = c.fetchone()

		# do something with the result
		return True if res else False

if __name__ == '__main__':
	db = DB('test', 'test1234','test')

	# let's use some hard-coded values for test:
	user_name = 'Maria'
	password = 'maria123'

	if db.authenticate(user_name=user_name, password=password):
		print('User is valid')
	else:
		print('Invalid user name or password')



