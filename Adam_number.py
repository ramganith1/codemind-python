n=int(input())
sq=n**2
a=str(sq)
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
sq2=rev**2
b=str(sq2)
if a==b[::-1]:
    print('True')
else:
    print('False')