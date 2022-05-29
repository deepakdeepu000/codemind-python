n=int(input())
d=0
r=0
k=0
while(n!=0):
    s=n%10
    d=d*10+s
    n=n//10
while(d!=0):
    f=d%10
    if(f==6 and k==0):
        f=9
        k+=1
    r=r*10+f
    d=d//10
print(r)