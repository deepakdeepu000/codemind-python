n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(n):
    c.insert(b[i],a[i])
for i in range(n):
    print(c[i],end=' ')