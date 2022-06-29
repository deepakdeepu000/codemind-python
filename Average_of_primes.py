def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1

n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,n):
    if prime(a[i]):
        s+=a[i]
        c+=1
av=s/c
print("%.2f"%av)