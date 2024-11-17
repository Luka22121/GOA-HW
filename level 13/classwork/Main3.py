list = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]

list_even = []

for i in list:
    if i % 2 == 0:
        list_even.append(i)
print(sum(list_even)/len(list_even))