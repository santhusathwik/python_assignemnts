# class Myclass:
#     def show(self):
#         print("Print method in Myclass")
# obj=Myclass()
# obj.show()

class Employee:
    def __init__(self,name,gender,salary):
        self.employeeName=name
        self.gender=gender
        self.salary=salary
    
    def get_info(self):
        print(f'Name:{self.employeeName}\nGender:{self.gender}')

# employee1=Employee("Yash","Male",9876)
# employee2=Employee("Yashasvi","Female",7654567)

# employee1.get_info()
# print()
# employee2.get_info()
# print()
# employee3.get_info()
# print()

employees=[]
n=int(input("Enter the no.of employees"))
for i in range(n):
    print(f"Enter details {i+1}")
    name=input("Enter Name")
    gender=input("Enter gender")
    salary=float(input("Enter salary"))
    employee=Employee(name,gender,salary)
    employees.append(employee)
    
for employee in employees:
    employee.get_info()