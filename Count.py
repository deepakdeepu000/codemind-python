n=int(input())
l=list(map(int,input().split()))
c,s=0,0
k=[]
for i in l:
    if i%2==0:
        c+=1
    else:
        s+=1
print(c,s)
    