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
x=list(map(int,input().split()))
for i in x:
    print(dig(i),end=" ")