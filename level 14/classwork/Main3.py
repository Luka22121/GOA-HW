J=[1,2,3,4,5,6,7,8,9,10]
L=[]
for i in J:
    if i%2==0:
        L.append(i)
print(sum (L)/len(L))