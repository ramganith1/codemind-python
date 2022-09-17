n=int(input())
l=0
for i in str(n):
    p=int(i)
    if l<p:
        l=p
print(l)