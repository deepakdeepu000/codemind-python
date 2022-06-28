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
s=0
for i in range(0,k):
    if prime(a[i]):
            s+=1
print(s)