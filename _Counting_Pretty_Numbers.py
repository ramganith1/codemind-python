T=int(input())
for t in range(T):
    L,R=map(int,input().split())
    n=0
    for i in range(L,R+1):
        k=i%10
        if k==2 or k==3 or k==9:
            n+=1
    print(n)