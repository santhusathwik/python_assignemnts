#  1) convert the prices in USD & Euro using appropriate function
#     PricesList_inr =[3000,56000,45000,2300]

# 2) student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
#     List the name which has more than 6 characters as lone_names list using appropriate function

# 3) products = [
#     {"name": "Laptop", "price": 92000},
#     {"name": "Smartphone", "price": 48000},
#     {"name": "Tablet", "price": 20000},
#     {"name": "Monitor", "price": 8000}
#     ]
#     Display the Product in ascending order based on the price of the product

# 4) You have a list of numbers. Filter out the odd ones, double the even numbers, and sort them in ascending order

# 5) You have a list of cities with their population data. Sort the cities in descending order of their population.
#    cities = [
#     {"name": "New York", "population": 8419600},
#     {"name": "Los Angeles", "population": 3980400},
#     {"name": "Chicago", "population": 2716000},
#     {"name": "Houston", "population": 2328000}
# ]

# 6) Extract Emails of Verified Users
#   You have a list of user records with email and a verification status. Extract the emails of verified users.
# 	users = [
#     {"email": "alice@example.com", "verified": True},
#     {"email": "bob@example.com", "verified": False},
#     {"email": "charlie@example.com", "verified": True},
#     {"email": "daisy@example.com", "verified": False}
# 	 ]

# 7) Calculate Discounts for Products
#  You have a list of products with their prices. Apply a 20% discount to products costing more than $100 and return the updated prices.

# 	products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Headphones", "price": 80},
#     {"name": "Smartphone", "price": 700},
#     {"name": "Monitor", "price": 150}
#    ]

# list out discounted products

# 8) sort Words by Length
#   Sort them in ascending order of their lengths.
# 	words = ["apple", "banana", "cherry", "date", "fig"]

# 9) write a program to remove the duplicates in the list
# # numbers3=[2,2,4,6,3,4,6,1]


def a1():
    PricesList_inr =[3000,56000,45000,2300]

    usdr=list(map(lambda x:round(x/86,2),PricesList_inr))
    euror=list(map(lambda x:round(x/90,2),PricesList_inr))

    n=len(PricesList_inr)

    for x in range(n):
        print(f"{PricesList_inr[x]}inr is {round(usdr[x],2)}usd and {round(euror[x],2)}euro")

    print("----------------------")
    print(f"INR:{PricesList_inr}")
    print(f"USD:{usdr}")
    print(f"EURO:{euror}")

#a1()

def a2():

    student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]

    lone_names=list(filter(lambda x: len(x)>6,student_name_list))
    print(lone_names)

#a2()

def a3():
    products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
    ]

    res=sorted(products,key=lambda x:x["price"])
    print(res)

# a3()

def a4():
    n=[1,2,3,4,5,6,7,8,9,0,11,12,13,14,54,64,36,4,5,3,7,899,999983735]
    res=list(filter(lambda x:x%2==0,n))
    res1=list(map(lambda x: x*2,res))
    res1.sort()
    print(res1)
# a4()

def a5():
    cities = [
    {"name": "New York", "population": 8419600},
    {"name": "Los Angeles", "population": 3980400},
    {"name": "Chicago", "population": 2716000},
    {"name": "Houston", "population": 2328000}
    ]
    res=sorted(cities,key=lambda x:-x["population"])
    print(res)
# a5()

def a6():
    users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]
    res=list(filter(lambda x: x["verified"]==True,users))
    print(res)
# a6()

def a7():
    products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
    res=list(filter(lambda x:x["price"]>100,products))
    print(res)
    res1=list(map(lambda x: x["price"]-0.2*x["price"],res))
    print(res1)
# a7()

def a8():
    words = ["apple", "banana", "cherry", "date", "fig"]
    res=sorted(words,key=lambda x:len(x)) 
    print(res)
# a8()

def a9():
    numbers3=[2,2,4,6,3,4,6,1]
    res=[]
    for i in numbers3:
        if i not in res:
            res.append(i)
    print(res)
# a9()
    