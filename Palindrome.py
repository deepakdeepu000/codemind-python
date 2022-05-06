a=int(input())
d=a
c=0
while a!=0:
    b=a%10
    a=a//10
    c=c*10+b
if c==d:
    print('True')
else:
    print('False')