n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
for i in range(n):
    if a[i]>=x and a[i]<=y:
        pass
    else:
        b.append(a[i])
if len(b)!=0:
    print(*b)
else:
    print(-1)