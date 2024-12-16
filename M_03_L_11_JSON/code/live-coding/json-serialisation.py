import json


def dict_to_json(python_object: dict) -> str:
    return json.dumps(python_object)


def json_to_dict(json_string: str) -> dict:
    return json.loads(json_string)


def main():
    # Пример объекта Python
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }

    # Преобразование объекта Python в строку JSON

    json_string = dict_to_json(data)
    print(type(json_string))

    python_object = json_to_dict(json_string)
    print(type(python_object))


if __name__ == '__main__':
    main()
