p=int(input())
q=int(input())
s1=0
s2=0
for i in range(1,p):
    if p%i==0:
        s1+=i
for i in range(1,q):
    if q%i==0:
        s2+=i
if s1==q and s2==p:
    print('Amicable')
else:
    print('Not Amicable')