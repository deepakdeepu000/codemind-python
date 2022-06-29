def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 0
    else:
        return 1
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        if prime(i):
            c+=1
print(c)