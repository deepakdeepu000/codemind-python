import math
def perf(n):
    r=math.sqrt(n)
    if int(r+0.5)**2==n:
        return 1
    return 0
n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(n):
    if perf(a[i]):
        s=s+a[i]
print(s)