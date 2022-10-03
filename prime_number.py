n=int(input())
t=False
if n>1:
    for i in range(2,n):
        if n%i==0:
            t=True
            break
if t:
    print('not a prime')
else:
    print('prime')