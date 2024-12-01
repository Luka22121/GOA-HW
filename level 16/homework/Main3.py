list = [-120, 1239, 23, 10, -234]
list1 = []
index = 0

while index < len(list):
    if list[index] < 0:
        list1.append(list[index])
    index+=1
print(list1)