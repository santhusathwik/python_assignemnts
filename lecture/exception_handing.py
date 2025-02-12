try:
    print("enter net sales")
    prev=float("Prior Period")
    curr=float("Current Period")
    change=(curr-prev)*100/prev

    if change>0:
        res=f"Sales increase {abs(change)}%"
    else:
        res=f"Sales increase {abs(change)}%"
    print(res)
except ValueError:
    print("Error! Please enter a number of net ")

