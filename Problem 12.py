def primedivisors(x):
    liste = list()
    while x % 2 == 0:
        liste.append(2)
        x //= 2

    for i in range(3, int(x ** 0.5) + 1, 2):
        while x % i == 0:
            liste.append(i)
            x //= i
    if x > 2:
        liste.append(x)

    return liste


a = 0
b = 1
while b < 999999:
    a = a +b
    b = b + 1

    print(a)

    liste = primedivisors(a)
    product = 1
    for i in set(liste):
        product *= (liste.count(i) + 1)

    if product > 10:
        break
