import pymongo
# client = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient("mongodb+srv://cluster0.qprcu.mongodb.net/", username="PythonCourse", password="1234")
db = client.python_course

db.todos.insert_many([
	{"title": "Learn Python", "done": True},
	{"title": "Learn Flask", "description":"Learn Flask to develop quick and easy web applications with the ability to scale up."},
	{"title": "Learn MongoDB", "due": "2021-12-31"}
])
