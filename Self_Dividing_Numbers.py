p=int(input())
q=int(input())
c=[]
for i in range(p,q+1):
    if i>0:
        n=i
        count=0
        while n>0:
            r=n%10
            if r:
                if i%r==0:
                    count+=1
            n=n//10
        if len(str(i))==count:
                c.append(i)
print(*c)