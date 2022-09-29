n=int(input())
l=len(str(n))
a=n**2
ld=a%pow(10,l)
if ld==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')