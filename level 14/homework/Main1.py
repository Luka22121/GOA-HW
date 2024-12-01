H=[]
for i in range(1,51):
    H.append(i)
for i in H:
    if i %2!=0:
        H.remove(i)
print(H)
