n=int(input())
a=list(map(int,input().split()))
s=n//2
c=0
p=0
for i in range(1,s+1):
    c=c+i
for i in range(n,s,-1):
    p=p+i
print(c)
print(p)
    