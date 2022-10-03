n=int(input())
a=list(map(int,input().split()))
av=0
for i in range(0,n):
    av+=a[i]/n
    k=abs(av)
print('%0.2f'%k)