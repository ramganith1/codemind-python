import math
n=int(input())
k=n
s=0
for i in str(k):
    t=int(i)
    f=math.factorial(t)
    s+=f
if s==n:
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')