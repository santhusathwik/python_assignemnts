customer= {
    "name":"Shikhar",
    "age":38,
    "phone":9876,
    "is_verified":True
    }
print(customer["name"])
print(customer.get('name'))

print(customer.get('birthdate','1-1-2005'))
print(customer)
keys=['name','age','city']
values=['Alice',25,'New York']
dict1=dict(zip(keys,values))
print(dict1)

#---------------------------------------------

#tuples

tuple=(1,2,3,4,1,2,3,3,3,3)
tuple1=(1)
tuple2=(1,)
print(f"{type(tuple)}\n{type(tuple1)}\n{type(tuple2)}")
print(tuple[3])
print(tuple.count(3)) #gives count frequency of element

#---------------------------------------------

#sets - doesnt allow duplicate values

a={"Rahul","Rani","Raju","Raghu"}
b={"Rahul1","Rani","Raju1","Raghu"}
print(a)   #items in a set do not appear in a stipulated manner, i.e., they can appear in a different order every time it is used
print(a) 
print(a) 
print(type(a))
print(a&b) #intersection
c=a.difference(b)
print(c)
d=a.copy()
print(d)
print(id(a))
print(id(d))
a.add(1)
print(a)
a.update([12,34,55])
print(a)
e=a.union(b)
print(e)
isub=a.issubset(b)
print(isub)
a.remove