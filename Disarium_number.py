x=int(input())
n=x
s=0
a=int(len(str(x)))
while n:
    r=n%10
    s+=(r**a)
    n//=10
    a-=1
if x==s:print(True)
else:print(False)