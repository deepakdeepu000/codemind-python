n=int(input())
b=1
c=0
while n!=0:
    a=n%10
    n//=10
    b*=a
    c+=a
r=b-c
print(r)
    