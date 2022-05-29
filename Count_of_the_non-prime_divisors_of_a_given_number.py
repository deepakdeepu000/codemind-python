def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 0
    else:
        return 1
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=prime(i)
print(c)