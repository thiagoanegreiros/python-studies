from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):

    __incremental_id = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

    def __str__(self):
        return f"Employee({self.name}, {self.id}, {self.position})"

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    @staticmethod
    def generate_employee_id() -> int:
        Employee.__incremental_id += 1
        return Employee.__incremental_id

class Developer(Employee):
    def __init__(self, name: str, projects: int):
        super().__init__(name, Employee.generate_employee_id())
        self.projects = projects
    
    def calculate_salary(self) -> float:
        return 3000 + (self.projects * 100)

class Manager(Employee):
    def __init__(self, name: str, teams: int):
        super().__init__(name, Employee.generate_employee_id())
        self.teams = teams
    
    def calculate_salary(self) -> float:
        return 5000 + (self.teams * 500)

def report_salaries(employees: List[Employee]):
    for employee in employees:
        print(f'{employee.name} ({employee.__class__.__name__}): ${employee.calculate_salary()}')

dev1 = Developer("Alice", projects=5)
dev2 = Developer("Bob", projects=3)
mgr1 = Manager("Carol", teams=2)

employees = [dev1, dev2, mgr1]
report_salaries(employees)
