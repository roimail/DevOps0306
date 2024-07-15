import requests

### run 66.py first, the Flask 'web-server'
# response = requests.post("http://localhost:5000/cars")
# assert response.text == "creating a new car"
# assert response.status_code == 201

### run 68.py first
# response = requests.post("http://localhost:5000/tasks")
#response = requests.delete("http://localhost:5000/tasks/1")

data = {
    "Title": "New Task",
    "description": "This is a new task created via requests."
}

response = requests.post("http://localhost:5000/tasks", json=data)
print(response.text)
