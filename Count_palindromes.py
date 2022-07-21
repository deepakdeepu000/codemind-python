def pal(n):
    k=n
    c=0
    while n!=0:
        b=n%10
        n=n//10
        c=c*10+b
    if c==k:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if pal(i):
        s+=1
print(s)