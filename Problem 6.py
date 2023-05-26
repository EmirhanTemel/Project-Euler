sum = 0

sqsum = 0

i = 0

while i <= 100:

    sum += i

    sqsum += i**2

    i += 1

print(sum**2-sqsum)