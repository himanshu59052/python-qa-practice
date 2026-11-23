import requests

data = {"title": "My first post", "body": "Learning Api testing", "userId":1}

response= requests.post("https://jsonplaceholder.typicode.com/posts",json=data)

print(response.status_code)
print(response.json())
