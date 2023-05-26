from math import sqrt

n = 2000000

integers = set(range(2, n))

for i in range(2, int(sqrt(n))):
    j = i ** 2
    while j < n:
        integers.discard(j)
        j += i

print(sum(list(integers)))
