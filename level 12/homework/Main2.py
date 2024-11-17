sum_even=0
sum_odd=0

for i in range(1,21):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd += i

    even=sum_even**5
    odd=sum_odd **5

    if even> odd:
        print(even)
    elif odd > even:
        print(odd)
else:
    print('Erti Da Igivea')
    