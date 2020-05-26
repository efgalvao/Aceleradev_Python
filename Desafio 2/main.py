from abc import ABC, abstractmethod

class Department:

    """
    Classe usada para definir a qual departamento o funcionário pertence.

    Atributos

    name: str
        Nome do departamento.
    code: int
        Código do departamento.
    """

    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    """
    Classe usada para criação de objetos da Classe Employee.

    Atributos

    code: int
        Código do funcionário.
    name: str
        Nome do funcionário.
    salary : int
        Salário do funcionário.
    hours :     
        Carga horária do funcionário

    """
    def __init__(self, code, name, salary):
        self._code = code
        self._name = name
        self._salary = salary
        self._hours = 8

    @abstractmethod
    def calc_bonus(self): # Função utilizada para calcular bonus de funcionários
        pass

    @abstractmethod
    def get_hours(self): # Função utilizada para retornar a carga horária do funcionário
        pass

class Manager(Employee):
    """
    Classe usada para criação de objetos da Classe Manager.

    Atributos

    code: int
        Código do funcionário.
    name: str
        Nome do funcionário.
    salary : int
        Salário do funcionário.
    department :     
        Departamento ao qual o funcionário pertence.

    """
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('managers', 1)

    def calc_bonus(self): # Função utilizada para calcular bonus de funcionários da classe Manager
        return self._salary * 0.15

    def get_hours(self): # Função utilizada para retornar a carga horária do funcionário
        return self._hours

    def get_department(self): # Função utilizada para retornar o departamento do funcionário
        return self._department.name

    def set_department(self, department): # Função utilizada para definir o departamento do funcionário
        self._department.name = department

class Seller(Employee):
    """
    Classe usada para criação de objetos da Classe Seller.

    Atributos

    code: int
        Código do funcionário.
    name: str
        Nome do funcionário.
    salary : int
        Salário do funcionário.
    department :     
        Departamento ao qual o funcionário pertence.
    sales : int
        Valor total de vendas do funcionário.

    """    
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._department = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self): # Função utilizada para calcular bonus de funcionários da classe Seller
        return (self.__sales * 0.15)

    def get_hours(self): # Função utilizada para retornar a carga horária do funcionário
        return self._hours

    def get_department(self): # Função utilizada para retornar o departamento do funcionário
        return self._department.name

    def set_department(self, department): # Função utilizada para definir o departamento do funcionário
        self._department.name = department

    def get_sales(self): # Função utilizada para retornar as vendas do funcionário
        return self.__sales

    def put_sales(self, value): # Função utilizada para cadastrar as vendas do Vendedor
        self.__sales += value
