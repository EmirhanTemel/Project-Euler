"""
x=1
y=2

evensum=0
i=0

while i<4000000:

    i = x + y
    x = y
    y = i

    if x%2==0:
        evensum+=x
    print(x,y,end="-")

print(evensum)
"""
from functools import reduce
x=1
y=2
i=0
ap=[x]

while i<4000000:

    x,y = y,x+y
    ap.append(x)
    i=y

a= reduce(lambda x,y: x+y, [i for i in ap if i%2==0])
print(a)

