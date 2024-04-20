from fastapi import APIRouter, Path
from model import Todo, TodoItem # model.py Todo baseModel(pydantic)

todo_router = APIRouter()

todo_list = []

# post route
# Create
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }

# get route
# Read
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }

"""
todo 처리를 위한 두개의 라우터를 사용한다.
첫 번째 라우트: todo_list에 todo를 추가하는 POST 메서드.
두 번째 라우트: 모든 todo 아이템을 todo_list에서 조회하는 GET 메서드
"""

# 경로 매개변수. 이전까지는 todo_list전체를 출력했으나, 하나의 todo만 추출하는 라우트를 만들어보자.
# Path class is provided by FastAPI
# Read
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }

# update
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }

# Delete
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todo deleted successfully."
    }

