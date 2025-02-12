class Add:
    def res(self,a,b):
        return a+b
class Mul(Add):
    def res(self,a,b):
        print(a*b)
        print(super().res(a,b))
    
obj=Mul()
obj.res(10,20)