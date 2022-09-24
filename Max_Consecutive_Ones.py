n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    if i==1:
        c+=1
    if i==0:
        if c>s:
            s=c
        c=0
if s<c:
    s=c
print(s)