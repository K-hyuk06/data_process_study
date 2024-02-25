import requests

url = "https://jsonplaceholder.typicode.com/comments"
res = requests.get(url)

print(res.json())