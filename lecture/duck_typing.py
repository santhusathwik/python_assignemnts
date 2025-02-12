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
    obj.walk()

d=duck()
fn(d)

h=horse()
fn(h)

c=cat()
# fn(c)     gives attribute error 

