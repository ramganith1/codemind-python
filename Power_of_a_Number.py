import math
x,y,M=map(int,input().split())
k=math.pow(x,y)
print(int(k%M))