name=[1,2,3,4,5,6,7,8,9,10]
sum=0
sum1=0
for person in name:
    if person%2==0:
        sum+=person
    else:
        sum1+=person
print(sum)
print(sum1)