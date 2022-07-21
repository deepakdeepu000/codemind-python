def rev(n):
    b=0
    while n!=0:
        a=n%10
        n=n//10
        b=b*10+a
    return b
n=int(input())
a=list(map(int,input().split()))
for i in  a:
    print(rev(i),end=" ")

    
        
        