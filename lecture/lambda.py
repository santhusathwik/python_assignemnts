# add_10=lambda x:x+10
# print(add_10(100))

def lambdaexample():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    product=lambda n1,n2:n1*n2
    print(f"The product is {product(n1,n2)}")

#lambdaexample()
# -------------------------------------------

def sales():
    n1=int(input("Enter price:"))
    n2=int(input("Enter quantity:"))
    product=lambda n1,n2:n1*n2
    print(f"The total price is {product(n1,n2)}")

#sales()
# -------------------------------------------

#lambda with condition

def evenorodd():
    n=int(input("Enter the number"))
    check=lambda n:"Even" if n%2==0 else "Odd"
    print(check(n))
#evenorodd()
# -------------------------------------------

#lambda with filter

def ex():
    n=[1,2,3,4,5,6,7,8,9,0]
    res=filter(lambda x:x>4,n)
    print(list(res))
# ex()
#--------------------------------------------

#lambda with map

def ex1():
    n=[1,2,3,4,5,6,7,8,9,0]
    res=map(lambda x:x>4,n)
    print(list(res))
# ex1()
#--------------------------------------------

#lambda with sort

def lsort():
    people=[("A",80),("B",70),("C",50),("D",60)]
    res=sorted(people,key=lambda x: x[1])    #the index represents 0-"A"[people here] and 1-80[key here]
    print(res)
lsort()