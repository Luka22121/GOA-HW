list = [1, 2, 2038, 2389, 1203]
first = list[0]

for i in list:
    if i < first:
        first = i
print(first)
