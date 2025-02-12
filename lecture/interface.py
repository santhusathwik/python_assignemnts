from abc import ABC,abstractmethod

# class Security(ABC):

#     @abstractmethod
#     def place_applied():
#         pass
    
#     def matrerial_used():
#         pass

# class Police(Security):
#     def place_applied(self):
#         print("Local Municiplaity")
#     def matrerial_used(self):
#         print("Gun")

# class Navy(Security):
#     def visit(self):
#         print("Go check the borderline")
#     def place_applied(self):
#         print("Contact Line")
#     def matrerial_used(self):
#         print("Rifle")

# def main():
#     police=Police()
#     police.place_applied()
#     police.matrerial_used()
#     print("-------------------------")
#     navy=Navy()
#     navy.place_applied()
#     navy.matrerial_used()
#     navy.visit()

# main()


class Abstractclass(ABC):
    def __init__(self,value):
        self.value=value
        print('Abstract class called')

    @abstractmethod
    def show(self):
        pass

class ConcreteClass(Abstractclass):
    def __init__(self, value,extra):
        super().__init__(value)
        self.extra=extra
        print("Concrete Class constructor called")
    def show(self):
        print(f'value: {self.value}, Extra: {self.extra}')

obj=ConcreteClass(10,'Extra data')
obj.show()