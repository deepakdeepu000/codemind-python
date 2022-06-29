n=int(input())
a=list(map(int,input().split()))
c=0
l=0
s=''
k=''

for i in a:
    for j in a:
        if i==j:
            c+=1
    if c==i:
        l+=1
        s+=str(i)
    c=0
if l==0:
    print("-1")
else:
    for i in s:
        if i not in k:
            k+=i
    for j in k:
        print(j,end=" ")

    
