m=int(input())
n=m*m
s=0
while n>0:
    r=n%10
    n=n//10
    s+=r
if s==m:
    print('Neon Number')
else:
    print('Not Neon Number')