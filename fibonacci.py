a=int(input())
b=[]
b.append(0)
b.append(1)
for i in range(2,a):
    b.append(b[i-2]+b[i-1])
for i in b:
    print(i,end=' ')