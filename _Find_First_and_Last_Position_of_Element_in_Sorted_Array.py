n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=[]
c=0
for i in range(0,n):
    if l[i]==k:
        c+=1
        s.append(i)
if c>0:
    for i in s:
        print(i,end=' ')
        break
    for i in s[::-1]:
        print(i,end=' ')
        break
else:
    print("-1 -1")