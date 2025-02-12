# single level inheritance
# class Father:
#     def __init__(self):
#         print("Father Class Constructor")
#     def showF(self):
#         print("Father Class Method")

# class Son(Father):
#     def __init__(self):
#         print("Son Class Constructor")
#     def showS(self):
#         print("Son Class Method")


# multi level inheritance
# class Father:
#     def __init__(self):
#         print("Father Class Constructor")
#     def showF(self):
#         print("Father Class Method")

# class Son(Father):
#     def __init__(self):
#         print("Son Class Constructor")
#     def showS(self):
#         print("Son Class Method")

# class Grandson(Son):
#     def __init__(self):
#         print("Grandson Class Constructor")
#     def showG(self):
#         print("Grandson Class Method")

# g=Grandson()
# g.showF()
# g.showS()
# g.showG()


#Hierarchical Inheritance

# class Father:
#     def __init__(self):
#         print("Father Class Constructor")
#     def showF(self):
#         print("Father Class Method")

# class Son(Father):
#     def __init__(self):
#         print("Son Class Constructor")
#     def showS(self):
#         print("Son Class Method")

# class Daughter(Father):
#     def __init__(self):
#         print("Daughter Class Constructor")
#     def showD(self):
#         print("Daughter Class Method")

# g=Daughter()
# g1=Son()
# g.showF()
# #g.showS()       #not possible
# g.showD()
# g1.showF()
# g1.showS()

#multiple inheritance

# class Father:
#     def __init__(self):
#         super().__init__()
#         print("Father Class Constructor")
#     def showF(self):
#         print("Father Class Method")

# class Mother:
#     def __init__(self):
#         super().__init__()
#         print("Mother Class Constructor")
#     def showM(self):
#         print("Mother Class Method")

# class Son(Father,Mother):
#     def __init__(self):
#         super().__init__()
#         print("Son Class Constructor")
#     def showS(self):
#         print("Son Class Method")

# g=Son()
# g.showS()
# g.showF()
# g.showM()