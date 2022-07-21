a,b=map(int,input().split())
c=list(map(int,input().split()))
s=0
for i in c:
    if i%b!=0:
        s+=1
print(s)