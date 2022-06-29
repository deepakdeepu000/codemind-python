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
b=[]
for i in range(0,a):
    n=int(input())
    for i in range(n,n+100):
        if prime(i):
            f=i
            break
    for i in range(n,0,-1):
        if prime(i):
            s=i
            break
    if abs(n-f)<abs(n-s):
        print(f)
    else:
        print(s)
    