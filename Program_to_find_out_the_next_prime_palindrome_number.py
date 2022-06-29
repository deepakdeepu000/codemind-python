def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
for i in range(a+1,a+10000):
    c=0
    j=i
    while i:
        b=i%10
        i=i//10
        c=c*10+b
    if c==j:
        if prime(c):
            print(c)
            break