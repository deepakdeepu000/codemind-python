def dig(n):
    if n==0:
        return 1
    c=0
    if n<0:
        n=-1*n
    while n:
        n=n//10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(dig(a[i]))
for i in range(n):
    if dig(a[i])==max(b):
        print(a[i],end=' ')