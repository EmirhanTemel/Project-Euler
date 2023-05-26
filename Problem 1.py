from functools import reduce
"""
i=0
sum=0

while i<1000:
    if i%3==0:
        sum+=i
    elif i%5==0:
        sum+=i
    i+=1
print(sum)
"""

res = reduce(lambda x,y: x+y,list(filter(lambda x: (x%3==0 or x%5==0), range(1,1000))))

a =sum([i for i in range(1,1000) if i%3==0 or i%5==0])
print(a)
print(res)

c = sum(set(range(0,1000,3))|set(range(0,1000,5)))
print(c)

b= sum([1,2,3,4])
print(b)



