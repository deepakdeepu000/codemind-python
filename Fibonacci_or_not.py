a=int(input())
b=[]
b.append(0)
b.append(1)
for i in range(2,100):
    b.append(b[i-2]+b[i-1])
if a in b:
    print(True)
else:
    print(False)