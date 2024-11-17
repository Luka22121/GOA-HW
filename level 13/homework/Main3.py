list=[1,2,3,4,5,6,7,8,9,10]
print(list)
G=int(input('Enter Number Betwin 1-10'))
if 1<=G<=10:
    list.remove(G)
    print(list)
else:
    print("pls enter a number Betwin 1-10")
    