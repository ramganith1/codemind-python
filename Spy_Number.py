n=int(input())
sum=0
pro=1
while n>0:
    r=n%10
    n=n//10
    sum+=r
    pro*=r
if sum==pro:
    print('Spy Number')
else:
    print('Not Spy Number')