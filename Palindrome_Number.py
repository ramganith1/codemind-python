T=int(input())
for i in range(T):
    m=int(input())
    rev=0
    n=m
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==m:
        print('True')
    else:
        print('False')