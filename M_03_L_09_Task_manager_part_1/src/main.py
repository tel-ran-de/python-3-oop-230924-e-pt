from Manager import Manager
import os


def get_help_info(command_list: dict):
    print('* '* 20)
    print('\n')
    print('Main menu')
    print('- ' * 20)
    for item in command_list.items():
        print(f'{item[0]}: {item[1]}')


def get_task_list(manager: Manager):
    task_list = manager.get_task_list()
    if len(task_list) > 0:
        print('\nTask list')
        for item in task_list:
            print(f'{item.id}: {item.title}')
    else:
        print('Task list is empty\n')


def check_config():
    if not os.path.isfile('config.yaml'):
        with open('config.yaml', mode='a'):
            pass


def main():
    check_config()
    manager = Manager('config.yaml')
    command_list = {
        '1': 'task list',
        '2': 'create new task',
        '3': 'delete task',
        'exit': 'exit'
    }
    while True:
        get_help_info(command_list)
        command = input('Input your command: ')
        if command in command_list:
            print(f'Command: {command_list[command]}\n')
            if command == 'exit':
                manager.save_task_list()
                break

            elif command == '1':
                get_task_list(manager=manager)

            elif command == '2':
                new_task_name = manager.create_task()
                print(f'New task: {new_task_name} created.')

            elif command == '3':
                task_id = input('Input task id to delete: ')
                try:
                    task_id = int(task_id)
                    manager.delete_task(task_id=task_id)
                except ValueError as e:
                    print('Can\'t convert this value to int')
        else:
            print('Unknown command.\n')


if __name__ == '__main__':
    main()
