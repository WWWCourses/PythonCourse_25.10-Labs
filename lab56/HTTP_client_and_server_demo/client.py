import requests


# --------------------------------- GET demo --------------------------------- #
# # base url
# url = "http://127.0.0.1:8000/index.html"

# # prepare headers
# headers = {
#   'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
# }

# # prepare query params
# query = {
#   'userName':'Ada',
#   'pass':'123',
# }

# # send request
# response = requests.get(url, headers=headers, params=query)

# print(response.headers)
# print(response.text)

# --------------------------------- POST demo -------------------------------- #
url = "http://127.0.0.1:8000/login"

# prepare headers
headers = {
  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

data = {
  'username':'python_course_test',
  'password':'python_course_test123'
}

# send request
response = requests.request('POST', url, headers=headers, data=data);
# response = requests.post(url, headers=headers, data=data)

if response.ok:
  print(response.text)

  # with open('./res.html','w') as f:
  #   f.write(response.text)