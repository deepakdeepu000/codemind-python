def rev(n):
    c=0
    while n!=0:
        a=n%10
        n=n//10
        c+=a
    return c
n=int(input())
a=rev(n)
if a>=10:
    b=rev(a)
    if b>=10:
        c=rev(b)
        print(c)
    else:
        print(b)
else:
    print(a)