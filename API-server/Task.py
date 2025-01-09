from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """
    This class represents a task for task management system
    """

    def __init__(self, title: str):
        self.__title = title
        self.__description = None
        self.__deadline = None
        self.__status = None
        self.__id = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if isinstance(title, str) & (title != ''):
            self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self.__description = description

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: datetime):
        if isinstance(deadline, datetime):
            self.__deadline = deadline

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status: str):
        self.__status = new_status

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id: int):
        self.__id = new_id
