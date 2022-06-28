def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1

k=int(input())
a=list(map(int,input().split()))
b=int(input())
s=0
for i in range(-1,k-1):
    if prime(a[i]):
        f=a[i]
        if f<=b:
            s+=1
print(s)