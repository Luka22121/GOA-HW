def gamqvavebi():
    n = int(input("შეიყვანე რიცხვი: "))
    g = []
    i = 1
    while i <= n:
        if n % i == 0:
            g.append(i)
        i += 1
    print(g)

