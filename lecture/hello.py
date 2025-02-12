print('Hello World!')

import keyword
print(keyword.kwlist)

help_message='''
Hi hello, this is an helpful message.
Please look into it.
'''

print(help_message)

message=r"C:\Users\santh\web\basics" #raw string
print(message)

fname="Santhu Sathwik"
lname="Goranti"

fullname=fname+" "+lname

greeting=f"Hi {fullname}"    #formatting string
print(greeting)

print(fullname[0])
print(len(fname))

print(fname[0:3])  #slicing

a=1
b=1.0
c=d=1
e,f,g,h=1,2,'hello','abcd'
i=h
print(i)

print(a,b,c,d,e,f,g,h)

res=a*b
print(f'Multiplication of {a} and {b} is {res}')

print(-9/4)
print(-9//4)    #floor division

print(10*'?')

print(a==b)

print(a<b and 1)
print(a==b and 1 and 0)
print(a<b or 1)

print(not(a==b))

s1="Hello, welcome to python"
print('to' in s1)
print('to' not in s1)


k=3.0
l=3
print(k is l)
print(a is not k)    #if both have same values like 3.0 and 3.0, python gives similar location to them


print(type(k))
print(type(fullname))

m=5
n=2
o=m/n
print(o)
print(type(o))
o=int(o)
print(o)
print(type(o))


str3="Hello python"
tup=tuple(str3)
print(tup)

print("hi","hello","hey",sep='$')
print("hi","hello","hey",end='$')

print() #new line

'''
rn=input("Enter the roll Number\n")
print(rn)

rn=input("Enter the roll Number\n")
print(rn)


print()

emp_name=input("enter emp names with space seperated\n").split('')           #split
for x in emp_name:
    print(x)

emp_name=input("enter emp names with space seperated\n").split('-')
for x in emp_name:
    print(x)

'''

lang='java'
'''
print(lang.upper())
print(lang.capitalize())
print(lang.lower())
'''

'''
while lang.capitalize() != "Python":
    lang=input("What is this programming language?")

    if lang.capitalize()=="Python":
        print(f"You are right it is {lang}")
        print("still here")
        
    else:
        print("Not good")
'''
for item in range(10):
    print(item)

''''
c=10
if c<18:
    c+=1
else:
    pass                                #pass is used when the definiton of any block is yet to be added
print(f'Ticket price is {ticket}')
'''
# age=int(input('Enter age'))
# ticket= 20 if age>=18 else 5    #ternery opertor
# print(f'Ticket price is {ticket}')

#function parameters

def student(name='Santhu',roll=21,location='Hyd'):
    print(f'Name:{name} \nRoll No.{roll} \nLocation:{location}')
    print('-------------')

student() #default parameters
student(name='Sathwik')
student(roll='15')
student(roll=15,name='Sathwik')
student('Sathwik',20,'Nzb')
# student(name='Sathwik',20,location='Nzb') not possible since positional argument i.e all the defined parameters should match
student(name='Sathwik',location='Nzb')
student('Sathwik',location='Nzb')


