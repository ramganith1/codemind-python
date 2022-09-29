import math
n=int(input())
sr=math.sqrt(n)
if int(sr+0.5)**2==n:
    print('True')
else:
    print('False')