def product(a,n):
    if n==1:
        print("0")
        return 
    i=1
    temp=1
    k=[1 for i in range(n)]
    for i in range(n):
        k[i]=temp
        temp*=a[i]
    temp=1
    for i in range(n-1,-1,-1):
        k[i]*=temp
        temp*=a[i]
    for i in range(n):
        print(k[i],end=" ")
n=int(input())
a=list(map(int,input().split()))
product(a,n)
    