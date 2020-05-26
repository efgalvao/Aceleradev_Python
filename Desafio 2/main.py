from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self._code = code
        self._name = name
        self._salary = salary
        self._hours = 8

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        return self._hours

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('managers', 1)

    def calc_bonus(self):
        return self._salary * 0.15

    def get_hours(self):
        return self._hours

    def get_departament(self):
        return self._department.name

    def set_department(self, department):
        self._department.name = department

class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return (self.__sales * 0.15)

    def get_hours(self):
        return self._hours

    def get_departament(self):
        return self._department.name

    def set_department(self, department):
        self._department.name = department

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value
