x = 100
b = list()

while x <= 999:

    y = 100

    while y <= x:

        product = x*y
        strp = str(product)
        a = list(strp)

        if a == list(reversed(a)):
            b.append(product)

        y += 1
    x += 1

print(max(b))