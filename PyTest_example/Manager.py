class Manager:
    def __init__(self, name: str):
        self.name = name
        self.__task_list = []

    def add_task(self, task: str):
        self.__task_list.append(task)

    def get_task_list(self):
        return self.__task_list

    def del_task(self, task: str):
        pass
