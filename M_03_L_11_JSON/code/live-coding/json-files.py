import json


def object_to_file(python_object, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(python_object, file, indent=4)


def file_to_object(file_path: str):
    with open(file_path, 'r') as file:
        python_object = json.load(file)
    return python_object


def main():
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }

    object_to_file(data, 'data.json')
    python_object = file_to_object('data.json')


if __name__ == '__main__':
    main()
