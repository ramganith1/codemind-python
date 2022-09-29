a,b=map(int,input().split())
temp=10**(b)
x=a%temp
temp1=int(str(a)[::-1])
y=temp1%temp
y=int(str(y)[::-1])
print(abs(x-y))