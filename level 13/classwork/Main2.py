list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even = 0
sum_odd = 0

for i in list: 
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(sum_even)
print(sum_odd)