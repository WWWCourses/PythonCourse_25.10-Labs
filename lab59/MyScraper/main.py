import requests

def save_html(content, filename):
	with open(filename,'w') as f:
		f.write(content)


base_url = 'http://127.0.0.1:44597/'

r = requests.get(base_url)

print(r.status_code)
# print(r.text)
save_html(r.text, 'test.html')
