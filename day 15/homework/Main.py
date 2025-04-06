print(" რეგისტრაცია")

s = input("შეიყვანე სახელი: ")
a = input("შეიყვანე ემაილი: ")
u = input("შეიყვანე პაროლი: ")

print(" რეგისტრაცია წარმატებით დასრულდა")

print(" შესვლა")


k = input("შეიყვანე ემაილი: ")
p = input("შეიყვანე პაროლი: ")

if k==a and p==u:
    print("Start Web Server")
else:
    print("Try agin")