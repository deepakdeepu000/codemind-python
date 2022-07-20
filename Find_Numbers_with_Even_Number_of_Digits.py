def count(a):
    c=0
    while a!=0:
        k=a%10
        c+=1
        a=a//10
    return c

n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if count(i)%2==0:
        k.append(i)
print(len(k))
        
        