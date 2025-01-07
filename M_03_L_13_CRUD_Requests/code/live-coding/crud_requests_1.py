# Через библиотеку requests выполнить GET запрос к корневому адресу.
# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить POST запрос к серверу – добавить в список два задания (разных).
# Выполнить GET запрос к серверу – получить задание с номером 2.
# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить PUT запрос к серверу – изменить одно из заданий.
# Выполнить GET запрос к серверу – получить список заданий.

# Смотрите на документацию к API по адресу http://127.0.0.1:8085/docs


import requests
import lorem


def get_root(address: str) -> (int, str):
    response = requests.get(address)
    return response.status_code, response.text


def get_task_list(root_address: str) -> (int, str):
    response = requests.get(root_address + '/todo')
    return response.status_code, response.json()


def add_new_task(root_address: str, task_id: int, task_name: str) -> (int, str):
    data = {
        'id': task_id,
        "item": task_name
    }
    response = requests.post(root_address + '/todo', json=data)
    return response.status_code, response.text


def update_task(root_address: str, task_id: int, new_text: str) -> (int, str):
    data = {
        "item": new_text
    }
    response = requests.put(root_address + '/todo/' + str(task_id), json=data)
    return response.status_code, response.text


def main():
    root_address = 'http://127.0.0.1:8085'

    response = get_root(address=root_address)
    print(response[0])
    print(response[1])

    response = get_task_list(root_address=root_address)
    print(response[0])
    for item in response[1]['todos']:
        print(item)

    for i in range(3):
        text = lorem.sentence()
        print(f'Adding new task id={i}: {text}')
        response = add_new_task(root_address=root_address, task_id=i, task_name=text)
        print(response[0])
        print(response[1])

    response = get_task_list(root_address=root_address)
    print(response[0])
    for item in response[1]['todos']:
        print(item)

    response = update_task(root_address=root_address, task_id=2, new_text='A new task text')
    print(response[0])
    print(response[1])

    response = get_task_list(root_address=root_address)
    print(response[0])
    for item in response[1]['todos']:
        print(item)


if __name__ == '__main__':
    main()
