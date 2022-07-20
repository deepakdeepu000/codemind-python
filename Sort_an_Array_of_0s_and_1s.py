def sort(a,n):
    c=0
    for i in range(n):
        if a[i]==0:
            c+=1
    for i in range(0,c):
        a[i]=0
    for i in range(c,n):
        a[i]=1
n=int(input())
a=list(map(int,input().split()))
sort(a,n)
print(*a)