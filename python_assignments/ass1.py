def login():
    c=3
    while c:
        username=input("Enter Username")
        password=input("Enter password")
        if username=='testuser' and password=='Password@123':
            print("Login Successful")
            break
        else:
            print("Login Invalid")
            c-=1
    if c==0:
        print("Attempts exceeded. Try again later")
#login()

def prime():
    c=0
    i=2
    n=int(input("Enter number"))
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if(c<2):
        print(f'{n} is a prime number')
    else:
        print(f'{n} is not a prime number')

#prime()

def salary():
    salary=int(input("Enter the salary"))
    allowance=int(input("Enter allowance"))
    gross=salary+allowance
    if salary<500000:
        net=(gross-(0.1*gross))
    else:
        net=(gross-(0.2*gross))
    print(f"Gross is{gross} and Net is {net}")

#salary()

def attendance():
    att=int(input("Enter attendance"))
    if att>=75:
        print("Allowed for exams")
    else:
        print("Not allowed for exams")
#attendance()