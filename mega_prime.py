def prime(a):
    c=0
    n=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        n=1
    else:
        n=0
    return n
a=int(input())
c=0
d=0
if prime(a)==1:
    while(a!=0):
        b=a%10
        a=a//10
        c+=1
        if prime(b)==1:
            d+=1
    if d==c:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')