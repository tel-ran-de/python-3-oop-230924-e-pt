# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить DELETE запрос к серверу – удалить одно задание.
# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить DELETE запрос к серверу – удалить все задания.
# Выполнить GET запрос к серверу – получить список заданий.

# Смотрите на документацию к API по адресу http://127.0.0.1:8085/docs


import requests


def get_task_list(root_address: str) -> (int, str):
    response = requests.get(root_address + '/todo')
    return response.status_code, response.json()


def del_one_task(root_address: str, task_id: int) -> (int, str):
    response = requests.delete(root_address + '/todo/' + str(task_id))
    return response.status_code, response.text


def delete_all_tasks(root_address: str) -> (int, str):
    response = requests.delete(root_address + '/todo')
    return response.status_code, response.text


def main():
    root_address = 'http://127.0.0.1:8085'

    response = get_task_list(root_address=root_address)
    print(response[0])
    for item in response[1]['todos']:
        print(item)

    response = del_one_task(root_address=root_address, task_id=2)
    print(response[0])
    print(response[1])

    response = get_task_list(root_address=root_address)
    print(response[0])
    for item in response[1]['todos']:
        print(item)

    response = delete_all_tasks(root_address=root_address)
    print(response[0])
    print(response[1])

    response = get_task_list(root_address=root_address)
    print(response[0])
    for item in response[1]['todos']:
        print(item)


if __name__ == '__main__':
    main()
