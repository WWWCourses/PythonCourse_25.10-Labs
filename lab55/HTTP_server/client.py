import requests

# base url
url = 'http://127.0.0.1:8080/'

# prepare headers
# headers = {
#   'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
# }

# prepare query params
query = {
  'userName':'Ada',
  'pass':'123',
}

# send request
response = requests.get(url, headers=headers)

# print response
if response.ok:
  print(response.text)
  print(response.headers)