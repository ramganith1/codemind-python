n=int(input())
f=0
s=1
if n<=0:
    print('series is',f)
else:
    print(f,s,end=' ')
    for i in range(2,n):
        next=f+s
        print(next,end=' ')
        f=s
        s=next