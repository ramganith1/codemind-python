n=int(input())
k=0
t=n
for i in range(1,n):
   if t%i==0:
       k+=i
if k==n:
    print('True')
else:
    print('False')