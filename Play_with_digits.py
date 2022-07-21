def rev(n):
    b=0
    while n!=0:
        a=n%10
        n=n//10
        b=b+a
    return b
n=int(input())
a=list(map(int,input().split()))
b=[]

for i in  a:
    b.append(rev(i))
print(sum(b))

    
        
        