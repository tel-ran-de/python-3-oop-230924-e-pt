import json
import os.path
import pickle
from Task import Task
import yaml


class Manager:
    def __init__(self, config_file_name: str):
        self.__config_file_name = config_file_name
        # Read config file
        with open(config_file_name, 'r') as stream:
            data_loaded: dict = yaml.safe_load(stream)

        self.__data_loaded = data_loaded

        if 'task_list_file' in data_loaded.keys():
            task_list_file = data_loaded['task_list_file']
        else:
            task_list_file = ''
        self.__task_list_file = task_list_file
        self.__task_list = self.__load_task_list(task_list_file)

    @staticmethod
    def __load_task_list(task_list_file: str):
        if os.path.isfile(task_list_file):
            with open(task_list_file, 'rb') as tasks_file:
                return pickle.load(tasks_file)
        else:
            return []

    def save_task_list(self):
        task_list_file = 'task_list.pkl'
        if self.__task_list_file == '':
            self.__data_loaded['task_list_file'] = task_list_file

        with open(task_list_file, 'wb') as tasks_file:
            pickle.dump(self.__task_list, tasks_file)

        print(f'Task list saved in file {self.__task_list_file}')

    def create_task(self):
        task_name = input('Input new task name: ')
        new_task = Task(title=task_name)
        max_id = 0
        for task in self.__task_list:
            if max_id <= task.id:
                max_id = task.id + 1
        return task_name

        new_task.id = max_id
        self.__task_list.append(new_task)

    def delete_task(self, task_id: int):
        flag = False
        for i, task in enumerate(self.__task_list):
            if task.id == task_id:
                self.__task_list.pop(i)
                print(f'Task with id: {task_id} deleted.')
                flag = True
        if not flag:
            print(f'Task with id = {task_id} not found.')

    def get_task_list(self):
        return self.__task_list
