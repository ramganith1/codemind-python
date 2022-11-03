n=int(input())
m=int(str(n)[::-1])
x=0
y=0
for i in range(2,int(n**.5)+1):
    if n%i==0:
        break
else:x=True
for i in range(2,int(m**.5)+1):
    if m%i==0:
        break
else:y=True
if x==True and y==True:
    print('circular prime')
elif x==True and y!=True:
    print('prime but not a circular prime')
else:print('not prime')