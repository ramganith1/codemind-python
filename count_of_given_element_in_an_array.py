n=int(input())
a=list(map(int,input().split()))
z=int(input())
count=0
for i in range(0,n):
    if a[i]==z:
        count+=1
print(count)