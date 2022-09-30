a,b=map(int,input().split())
s=0
for j in range(a):
    x=list(map(int,input().split()))
    for i in range(len(x)):
        if j==0 or j==(a-1):
            s=s+x[i]
        else:
            if i==0 or i==(len(x)-1):
                s=s+x[i]
print(s)