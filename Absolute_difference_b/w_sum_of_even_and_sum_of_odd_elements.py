n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in a:
    if i%2==0:
        c+=i
for i in a:
    if i%2!=0:
        s+=i
print(abs(c-s))