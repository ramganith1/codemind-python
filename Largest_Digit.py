N=int(input())
l=0
while N>0:
    r=N%10
    if l<r:
        l=r
    N=N//10
print(l)