a=int(input())
k=0
c=0
d=0
for i in range(1,a+1):
    if(a%i==0):
        k+=1
while(a!=0):
    b=a%10
    a=a//10
    c=c*10+b
for j in range(1,c+1):
    if(c%j==0):
        d+=1
if k==2 and d==2:
    print('circular prime')
elif k==2 and d!=2:
    print('prime but not a circular prime')
else:
    print('not prime')