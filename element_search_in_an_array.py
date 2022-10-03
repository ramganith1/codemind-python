n=int(input())
a=list(map(int,input().split()))
c=int(input())
p=0
for i in range(0,n):
    if a[i]==c:
        p=1
if p==1:
    print('True')
else:
    print('False')