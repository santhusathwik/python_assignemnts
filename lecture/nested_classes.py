class Array:
    def _init_(self):
        self.name='Rahul'
        self.gn=self.Gun()

    def show(self):
        print('Name:',self.name)
    
    class Gun:
        def _init_(self):
            self.name='AK47'
            self.capacity='75 Rounds'
            self.length='34.4 ln'

        def disp(self):
            print('Gun Name',self.name)
            print('Capacity:',self.capacity)
            print('Length:',self.length)

            
a=Array()
print(a.name)
print()
a.show()

print()
print(f'a.gn={a.gn}')
print(f'a.gn.name={a.gn.name}')
g=a.gn
print(g.name)
print(g.capacity)
print(g.length)
print()
g.disp()