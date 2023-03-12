import datetime

from dateutil.relativedelta import relativedelta


class Person:
    def __init__(self, id, name, birthday):
        self.__id = id
        self.__name = name
        self.__birthday = birthday

    def __str__(self) -> str:
        return  str(self.__id) + " " + self.__name + " " + str(self.__birthday)

    def get_age(self):
        return 0
