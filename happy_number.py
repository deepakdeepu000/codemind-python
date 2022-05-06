a=int(input())
c=0
while a>=10:
    c=0
    while a!=0:
        b=a%10
        a=a//10
        c+=b*b
    a=c
    
if a==1 or a==7:
    print('True')
else:
    print('False')