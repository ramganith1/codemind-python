startingvalue=int(input())
endingvalue=int(input())
for i in range(startingvalue,endingvalue+1):
    rev=0
    n=i
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==i:
        print(i,end=' ')