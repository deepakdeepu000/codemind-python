def rev(n):
    c=0
    while n!=0:
        b=n%10
        n=n//10
        c+=b
    return c
n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    s.append(rev(i))
print(sum(s))