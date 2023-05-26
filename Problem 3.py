"""
i = 2
num = 600851475143
while i<num:
    if num%i==0:
        c = 1
        p = 0
        while c <= i:
            if i % c == 0:
                p += 1
            c += 1

        if p <= 2:
            print(i, end=" ")
    i += 1
"""

"""
a = lambda x: [i for i in range(1, x) if x % i == 0]
b = list(filter(lambda x: len(a(x)) < 2, a(100)))

print(b)
"""


import math
x = 600851475143
for i in range(2, math.ceil(math.sqrt(x))):
    if x % i == 0:
        if i < x:
            x //= i
        else:
            print(i)
            break
