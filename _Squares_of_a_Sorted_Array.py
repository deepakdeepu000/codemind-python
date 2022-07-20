n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    s=i*i
    k.append(s)
c=sorted(k)
print(*c)
