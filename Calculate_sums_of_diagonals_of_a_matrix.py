n=int(input())
a,b=0,0
j=n-1
for i in range(n):
    l=list(map(int,input().split()))
    a+=l[i]
    b+=l[j]
    j-=1
print("Principal Diagonal:%d"%a)
print("Secondary Diagonal:%d"%b)