# products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
# products=products.split()
# arr={}
# for i in products:
#     if i in arr:
#         arr[i]+=1
#     else:
#         arr[i]=1
# print(arr)
#------------------------------------
# initial_stock = {"apple": 50,"banana": 100,"orange": 75}
# sold_item = {"apple": 10, "banana": 20, "orange": 15}
# for i in initial_stock:
#     initial_stock[i]=initial_stock[i]-sold_item[i]
# print(initial_stock)
#------------------------------------
# sales_data = [
#     {"region": "North", "sales": 15000},
#     {"region": "South", "sales": 8000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000}
# ]
# res={}
# for i in sales_data:
#     if i['region'] in res:
#         res[i['region']]+=i['sales']
#     else:
#         res[i['region']]=i['sales']
# print(result)
#------------------------------------
# pno=input("enter your mobile number: ")
# arr={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
# for i in pno:
#     print(arr[i])