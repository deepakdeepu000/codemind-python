a=str(input())
c=0
m=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c+=1
    if c==1:
        m+=1
        print(i)
        break
    c=0
if m==0:
    print("-1")