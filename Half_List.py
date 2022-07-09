n=int(input())
a=list(map(int,input().split()))
b=n//2
for i in range(n-1,b-1,-1):
    print(a[i],end=" ")
for i in range(0,b):
    print(a[i],end=" ")
