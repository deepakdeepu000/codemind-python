def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r
n=int(input())
d=n
b=0
while d!=0:
    a=d%10
    b=b+fact(a)
    d=d//10
if n==b:
    print('The number {0} is a strong number'.format(n))
else:
    print('The number {0} is not a strong number'.format(n))
