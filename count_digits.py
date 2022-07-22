def dig(n):
    c=0
    if n==0:
        return 1
    elif n<0:
        n = n*-1
    while(n):
        n=n//10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    s.append(dig(i))
print(*s)