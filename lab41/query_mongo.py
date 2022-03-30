from pymongo import MongoClient
from datetime import datetime, date

client = MongoClient("mongodb://localhost:27017")
db = client.python_course


# # write the title of all documents in the collection
# for doc in db.todos.find({},{'title':1,'_id':0} ):
# 	print(doc['title'])


# some_date = datetime.strptime('2022-01-01', '%Y-%m-%d')
# # some_date = datetime.fromisoformat('2022-01-01')

# for doc in db.todos.find(
# 	{'$and':[
# 		{"dueDate":{"$gt": some_date}},
# 		{'completed':True}
# 	]},
# 	{'_id':0, 'title':1, 'dueDate':1, 'completed':1}
# ):
# 	print(doc)

# res = db.todos.update_one({'title':'Learn'}, {'$set':{'completed':False}})
# print(dir(res))
# print(res.modified_count)

# res = db.todos.delete_many(
#   {"title": "Learn Python"}
# )
# print(res.deleted_count)


# for doc in db.todos.find(
# 	{'title':{'$regex':'learn', '$options':'i' }},
# 	{'title':1, '_id':0} ):
# 		print(doc)


db.todos.create_index([
  ("title","text")
])

for doc in db.todos.find(
	{ "$text": { "$search": "learn" } },
	{'title':1, '_id':0} ):
	print(doc)