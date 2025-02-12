from abc import ABC,abstractmethod
class Employee(ABC):
    emp={}
    @abstractmethod
    def work():
        pass
    @abstractmethod
    def get_salary():
        pass
class Manager(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(f"{self.name} Managing work, employees")
    def get_salary(self):
        print(f"Manager salary={self.salary}")
class Developer(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(f"{self.name} Works for the capgemini company")
    def get_salary(self):
        print(f"Employee salary is {self.salary}")
class Department(Manager,Developer):
    def hire(self, employee: Employee):
        Employee.emp[employee.name]=[employee.salary]
    def fire(self, employee: Employee):
        del Employee.emp[employee.name]
    def get_total_salary(self):
        print(f"{sum(Employee.emp.values())}")
    def show_employee_details(self):
        print(f"{Employee.emp}")
manager=Manager("chemesh",69)
manager.work()
manager.get_salary()
dev=Developer("kd",96)
dev.work()
dev.get_salary()
dep=Department(manager)
dep.get_total_salary()