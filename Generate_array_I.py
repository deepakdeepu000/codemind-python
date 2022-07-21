x = int(input())
a = list(map(int,input().split()))
b=[]
c=[]
d=[]
for i in range(0,x,2):
    b.append(str(a[i]))
for j in range(1,x+1,2):
    c.append(a[j])
m = len(b)
k=0
if k!=m:
    for i in c:
        s = b[k]*i
        d.append(s)
        k+=1
for res in d:
    z = list(res)
    for t in z:
        print(t,end=" ")