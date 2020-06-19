from abc import ABC, abstractmethod

class Department:
    """
    Class used to define which department the employee belongs to.

    Attributes

    name: str
        Department name.
    code: int
        Department code.
    """

    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee(ABC):
    """
    Class used to create objects of the Employee Class.

    Attributes

    code: int
        Employee code.
    name: str
        Employee name.
    salary : int
        Employee salary.
    workload :     
        Employee workload.

    """
    def __init__(self, code, name, salary):
        self._code = code
        self._name = name
        self._salary = salary
        self._workload = 8

    @abstractmethod
    def calc_bonus(self): # Function used to calculate employee bonuses
        pass

    @abstractmethod
    def get_hours(self): # Function used to return the employee's workload
        pass

class Manager(Employee):
    """
    Classe usada para criação de objetos da Classe Manager.

    Attributes

    code: int
        Employee code.
    name: str
        Employee name.
    salary : int
        Employee salary.
    department :     
        Employee dapartment.

    """
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('managers', 1)

    def calc_bonus(self): # Function used to calculate bonus for Manager class employees
        return self._salary * 0.15

    def get_hours(self): # Function used to return the employee's workload
        return self._workload

    def get_department(self): # Function used to return the employee's department
        return self._department.name

    def set_department(self, department): # Function used to define the employee's department
        self._department.name = department

class Seller(Employee):
    """
    Class used to create objects of the Seller Class.

    Attributes

    code: int
        Employee code.
    name: str
        Employee name.
    salary : int
        Employee salary.
    department :     
        Employee department.
    sales : int
        Total employee sales value.

    """    
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self): # Function used to calculate bonus for Seller class employees
        return (self.__sales * 0.15)

    def get_hours(self): # Function used to return the employee's workload
        return self._workload

    def get_department(self): # Function used to return the employee's department
        return self._department.name

    def set_department(self, department): # Function used to define the employee's department
        self._department.name = department

    def get_sales(self): # Function used to return employee sales
        return self.__sales

    def put_sales(self, value): # Function used to register Salesperson sales
        self.__sales += value
