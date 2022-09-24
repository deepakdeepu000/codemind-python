a,b=map(int,input().split())
p=[]
q=[]
r=[]
s=[]
t=[]
for i in range(a):
    k=list(map(int,input().split()))
    p.append(k[0])
    q.append(k[1])
    if b>2:
        r.append(k[2])
    if b>3:
        s.append(k[3])
    if b>4:
        t.append(k[4])
print(max(p))
if b>=2:
    print(max(q))
if b>=3:
    print(max(r))
if b>=4:
    print(max(s))
if b>=5:
    print(max(t))
        