a = int(input("Dene: "))

i = 1
limit = 1

while i <= a:

    limit *= i
    i += 1

j = 1

while j <= limit:

    c = 0
    x = a
    while x > c:
        if j % x != 0:
            break
        else:
            x -= 1
        if x == 1:
            print(j)
            quit()
    j += 1