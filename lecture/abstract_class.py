from abc import ABC,abstractmethod

class Father(ABC):
    def display(self):
        print("I am display from father abstract class")

    @abstractmethod
    def myabstractmethod(self):
        pass

class Son(Father):
    def myabstractmethod(self):
        print('Hello from child implementing abstract method from father')

    def show(self):
        print('I am from child class')

c=Son()
c.display()