a,b,c=map(int,input().split())
s=0
for i in range(a,b+1):
    if i%c==0:
        s+=1
print(s)