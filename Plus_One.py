n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    c=c*10+i
c+=1
s=str(c)
for i in s:
    print(i,end=" ")