import requests
from fastapi import FastAPI

class Todo():
    userId: int
    id: int
    title: str
    completed: bool

    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed
    
    def __repr__(self):
        return f"Todo(Id='{self.id}', Title='{self.title}')"

app = FastAPI()

@app.get("/myapi")
def read_root():

    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    items = [Todo(item['userId'], item['id'], item['title'], item['completed']) for item in response.json()]

    return items

print('aaa')