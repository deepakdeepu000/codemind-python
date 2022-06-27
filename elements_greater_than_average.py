n = int(input())
a = list(map(int,input().split()))
b=sum(a)//n
c=0
for i in range(0,n):
    if a[i]>=b:
        c+=1
print(c)