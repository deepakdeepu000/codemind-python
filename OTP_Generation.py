a=str(input())
b=int(a)
c=0
while b!=0:
    d=b%10
    b=b//10
    c=c*10+d
while c!=0:
    e=c%10
    c=c//10
    if e%2!=0:
        print(e*e,end='')