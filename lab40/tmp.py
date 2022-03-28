import json,os

print( os.getcwd() )

user = {
	'name':'Ada',
	'age':23
}

with open('./user_data.json','w') as f:
	json.dump(user,f)



