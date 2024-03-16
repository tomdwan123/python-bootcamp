import requests, bs4

url = 'https://www.python.org/a.html'
response = requests.get(url)
print(type(response))

print(response.status_code)
print(response.ok)
print(response.content.decode())
print(response.text)
print(response.encoding)
print(response.headers)