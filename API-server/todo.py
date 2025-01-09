from fastapi import APIRouter, Path

from model import Todo, TodoItem

from Manager import Manager
from Task import Task
import logging


todo_router = APIRouter()

todo_list = []
manager = Manager('config.yaml')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@todo_router.post("/todo")
async def add_todo(task_name: str) -> dict:
    manager.create_task(task_name)
    # logger.debug(f'New task created: {new_task.title}')
    return {
        "message": f"Todo with {task_name} successfully."
    }


@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        'todos': manager.get_task_list()
    }

#
# @todo_router.get("/todo/{todo_id}")
# async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
#     for todo in todo_list:
#         if todo.id == todo_id:
#             return {
#                 "todo": todo
#             }
#     return {
#         "message": "Todo with supplied ID doesn't exist."
#     }
#
#
# @todo_router.put("/todo/{todo_id}")
# async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
#     for todo in todo_list:
#         if todo.id == todo_id:
#             todo.item = todo_data.item
#             return {
#                 "message": "Todo updated successfully."
#             }
#     return {
#         "message": "Todo with supplied ID doesn't exist."
#     }
#
#
@todo_router.delete("/todo")
async def delete_single_todo(task_id: int):
    manager.delete_task(task_id)
#
#
# @todo_router.delete("/todo")
# async def delete_all_todo() -> dict:
#     todo_list.clear()
#     return {
#         "message": "Todos deleted successfully."
#     }
