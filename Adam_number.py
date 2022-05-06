a=int(input())
b=a*a
c=0
while a!=0:
    d=a%10
    a=a//10
    c=c*10+d
e=c*c
f=0
while e!=0:
    g=e%10
    e=e//10
    f=f*10+g
if f==b:
    print('True')
else:
    print('False')