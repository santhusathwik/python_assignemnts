from functools import reduce
names=["Shikhar","Rohit","Kohli","Pant"]
print(names[0])
print(names[-2])

print(names[1:3])
print(names[1:])
print(names[:3])
print(names[:])
print(names)


n=[1,2,3,4,6,7,5,8,34,3,2,4,56,66,6]
max=0
for i in n:
    if i>max:
        max=i
print(max)

#methods
 #append, remove, clear, copy, extend, concatenation, count, sort, reverse, index, slice, pop

n.pop()
print(n)

n.append(1)
print(n)

n.remove(1)
print(n)

n.sort()
print(n)

n.reverse()
print(n)

a=n.index(7)
print(a)

a=[1,2,3,4]
b=a+n
print(b)

a.extend(n)
print(a)

#reduce() using lambda is used to apply a rolling computation to sequential pair of values 

product = reduce(lambda x,y:x*y,n)
print(product)