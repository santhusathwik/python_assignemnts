class duck:
    def walk(self):
        print("Duck quacks")
class horse:
    def walk(self):
        print("Horse neighs")
class cat:
    def eat(self):
        print("Cat meows")

def fn(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'eat'):
        obj.eat()

d=duck()
fn(d)

h=horse()
fn(h)

c=cat()
fn(c)     #doesnt give attribute error 

