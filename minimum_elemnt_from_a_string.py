s=list(map(str,input().split()))
s=s[-1]
a=min(s)
m=a.lower()
if s.count(m)!=0:
    print(m)
else:
    print(a)