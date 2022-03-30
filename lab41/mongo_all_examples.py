import pymongo
from datetime import datetime

# ------------------------- Connect to MongoDB Server ------------------------ #
# connect to MongoDB server:
client = pymongo.MongoClient("mongodb://localhost:27017")

# ----------------------- Switch context to a database ----------------------- #
# get "python_course" database:
db = client.python_course

# ------------------- Show all Collections in the database: ------------------ #
# get all collections in the database:
collections = db.list_collection_names()
# print(collections)

# ---------------------------------- Create ---------------------------------- #
# # insert a new document into "todos" collection:
# res = db.todos.insert_one({"title": "Learn MongoDB", "done": False})

# # get the id of the inserted document:
# print(res.inserted_id)

# # insert multiple documents into "todos" collection:
# res =  db.todos.insert_many([
# 	{
# 		"title": "Learn Python",
# 		"completed": True,
# 		"dueDate": datetime.fromisoformat("2021-07-01"),
# 		"priority": 1
# 	},
# 	{
# 		"title": "Learn Flask",
# 		"description":"Learn Flask to develop quick and easy web applications with the ability to scale up.",
# 		"completed": True,
# 		"dueDate": datetime.fromisoformat("2022-01-12"),
# 		"priority": 2
# 	},
# 	{
# 		"title": "Learn MongoDB",
# 		"completed": False,
# 		"dueDate": datetime.fromisoformat("2022-01-12"),
# 		"priority": 1
# 	},
# 	{
# 		"title": "Learn PyQT",
# 		"completed": False,
# 		"dueDate": datetime.fromisoformat("2021-12-01"),
# 		"priority": 2
# 	}
# ])
# print(res.inserted_ids)

# # insert multiple documents with different shape into "todos" collection:
# res = db.todos.insert_many([
# 	{"title": "Learn Python", "done": True},
# 	{"title": "Learn Flask", "description":"Learn Flask to develop quick and easy web applications with the ability to scale up."},
# 	{"title": "Learn MongoDB", "due": "2021-12-31"}
# ])
# print(list(db.todos.find())[-3:-1])


# ----------------------------------- Read ----------------------------------- #
# # find first document in "todos" collection:
# print(db.todos.find_one())

# # find all documents in "todos" collection:
# for todo in db.todos.find():
# 	print(todo)

# --------------------------- Filter and Projection -------------------------- #
# completed = db.todos.find({'completed':False})
# print(list(completed))

# python_completed = db.todos.find(
# 	{
# 		'$and':[
# 			{'done':True},
# 			{'title':{'$regex': 'learn', '$options': 'i' }}
# 		]
# 	},
# 	{
# 		'title':1,'done':1,'_id':0
# 	}
# )

# # get all completed tasks and return all fields, except "_id"
# completed1 = db.todos.find({'completed':False}, {"_id":0})

# # get all completed tasks and return only "title" field
# completed2 = db.todos.find({'completed':False}, {"title":1,"_id":0})

# print(list(completed1))
# print(list(completed2))

# -------------------------- Text Indexes and Search ------------------------- #
db.todos.create_index([
	("title","text")
])

res = db.todos.find({ "$text": { "$search": "python" } })

print(list(res))