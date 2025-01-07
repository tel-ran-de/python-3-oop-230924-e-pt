# Через библиотеку requests выполнить GET запрос к корневому адресу.
# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить POST запрос к серверу – добавить в список два задания (разных).
# Выполнить GET запрос к серверу – получить задание с номером 2.
# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить PUT запрос к серверу – изменить одно из заданий.
# Выполнить GET запрос к серверу – получить список заданий.

# Смотрите на документацию к API по адресу http://127.0.0.1:8085/docs

import requests
# def get_root(address: str) -> (int, str):
#     response = requests.get(address)
#     return response.status_code, response.text

# def get_task_list(root_address: str) -> (int, str):
#     response = requests.get(root_address + '/todo')
#     return response.status_code, response.json()

def main():
    # root_address = 'http://127.0.0.1:8085'

    # response = get_root(address=root_address)
    # print(response[0])
    # print(response[1])

    # response = requests.get(root_address + "/todo")
    # print(response)
    # print(response.status_code)
    # print(response.json())
    #
    # response = requests.post(root_address + "/todo", json = {"id": 0,"item": "string"})
    # print(response.status_code, response.text)
    #
    # response = requests.get(root_address + "/todo")
    # print(response)
    # print(response.status_code)
    # print(response.json())
    #
    # response = requests.delete(root_address + "/todo/0" )
    # response = requests.get(root_address + "/todo")
    # print(response)
    # print(response.status_code)
    # print(response.json())

    # response = requests.put(root_address + "/todo" + str("id"), json = {"item": "string"})
    # response = requests.get(root_address + "/todo")
    # print(response)
    # print(response.status_code)
    # print(response.text)
    # import requests

    # Базовый URL  сервера
    base_url = "http://127.0.0.1:8085"

    # Выполнить GET запрос к корневому адресу
    response = requests.get(base_url)
    print("GET /:", response.text)

    # Выполнить GET запрос к серверу – получить список заданий
    response = requests.get(f"{base_url}/tasks")
    print("GET /tasks:", response.json())

    # Выполнить POST запрос к серверу – добавить в список два задания (разных)
    task1 = {"title": "Задача 1", "description": "Описание задачи 1"}
    task2 = {"title": "Задача 2", "description": "Описание задачи 2"}
    response = requests.post(f"{base_url}/tasks", json=task1)
    print("POST /tasks (task1):", response.json())
    response = requests.post(f"{base_url}/tasks", json=task2)
    print("POST /tasks (task2):", response.json())

    # Выполнить GET запрос к серверу – получить задание с номером 2
    response = requests.get(f"{base_url}/tasks/2")
    print("GET /tasks/2:", response.json())

    # Выполнить GET запрос к серверу – получить список заданий
    response = requests.get(f"{base_url}/tasks")
    print("GET /tasks:", response.json())

    # Выполнить PUT запрос к серверу – изменить одно из заданий
    updated_task = {"title": "Обновленная задача 1", "description": "Обновленное описание задачи 1", "completed": True}
    response = requests.put(f"{base_url}/tasks/1", json=updated_task)
    print("PUT /tasks/1:", response.json())

    # Выполнить GET запрос к серверу – получить список заданий
    response = requests.get(f"{base_url}/tasks")
    print("GET /tasks:", response.json())


if __name__ == '__main__':
    main()
