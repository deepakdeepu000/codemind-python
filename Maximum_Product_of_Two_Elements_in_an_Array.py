a=list(map(int,input().split()))
b=max(a)
c=min(a)
a[a.index(b)]=c
s=max(a)
print((b-1)*(s-1))
