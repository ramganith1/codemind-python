def com_gcd(a,b):
    while b:
        a,b=b,a%b
    return a

a,b=map(int,input().split())
hcf=com_gcd(a,b)
print(hcf)