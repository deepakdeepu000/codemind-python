n=int(input())
b=0
d=0
f=0
while n!=0:
    a=n%10
    n=n//10
    b+=a
if b>=10:
    while b!=0:
        c=b%10
        b=b//10
        d+=c
    if d>=10:
        while d!=0:
            e=d%10
            d=d//10
            f+=e
        print(f)
    else:
        print(d)
else:
    print(b)