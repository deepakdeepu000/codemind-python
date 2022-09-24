n=int(input())
l=list(map(int,input().split()))
a=int(input())
k=list(map(int,input().split()))
q=int(input())
c=0
for i in range(n):
    if(l[i]<=q<=k[i]):
        c+=1
print(c)