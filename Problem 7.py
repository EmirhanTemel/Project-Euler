i = 2
primecount = 0
while i < 999999999999999999999999999:

    c = 1
    p = 0

    while c <= i:
        if i % c == 0:
            p += 1
        if p > 2:
            break
        c += 1


    if p <= 2:
        primecount += 1

    if primecount == 10001:
        print(i)
        quit()

    i += 1