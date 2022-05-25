import os

root = './front-end////'
path = 'login.html'

filename =  os.path.normpath(os.path.join(root, path))
print(filename)