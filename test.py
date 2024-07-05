import requests

url = "http://localhost:3000"
test = "www.google.com"

file_path= "/sites.txt"

response = requests.post(url, files = {"site":test})

print(response.status_code)
print(response.text)
