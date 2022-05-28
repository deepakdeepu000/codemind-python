def s_div(n):
    a=n
    b=n
    c=0
    s=0
    while a!=0:
        d=a%10
        a=a//10
        c+=1
    while b!=0:
        f=b%10
        b=b//10
        if f==0:
            continue
        if n%f==0:
            s+=1
    if c==s:
        print(n,end=' ')
a=int(input())
b=int(input())
for i in range(a,b+1):
    s_div(i)
