# class Example:
#     def __init__(self,name):
#         self.name=name  #public variable
    
#     def display(self):  #public method
#         print('Name',self.name)

# ex=Example('Santhu')
# print(ex.name)
# ex.display()

#----------------------------------------------

# class Example:
#     def __init__(self,salary):
#         self.__salary=salary    #private variable
    
#     def __display(self):    #private method
#         print(f"Salary {self.__salary}")

#     def acceess_private(self):
#         self.__display()    #allowed inside class

# obj=Example(5000)
# #obj.__display() #Attribute error
# obj.acceess_private()

# print(obj._Example__salary) #discouraged way

#----------------------------------------------

# class Example:
#     def __init__(self,age):
#         self._age=age
#     def _display(self):
#         print(f"Age:{self._age}")

# class Ex(Example):
#     def show(self):
#         print(f"Accessing protected {self._age}")
#         self._display()

# objsub=Ex(25)
# print(f"Accessing age from protected variable {objsub._age}")
# objsub._display()

# obj=Example(26)
# print(f"Accessing age through base class object {obj._age}")
# obj._display()
