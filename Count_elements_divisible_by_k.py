n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%m==0:
        c+=1
print(c)