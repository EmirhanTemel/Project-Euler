liste1 = dict()
for n in range(2, 1000000):
    c = 0
    key = n
    while n != 1:
        c += 1
        if n % 2 == 0:
            n //= 2

        else:
            n = 3 * n + 1

    liste1[str(key)] = c

max_value = max(liste1, key=liste1.get)

print(max_value)
