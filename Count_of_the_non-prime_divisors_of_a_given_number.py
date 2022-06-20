def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 0
    else:
        return 1
a=int(input())
count=0
for j in range(1,a+1):
    if a%j==0:
        count+=prime(j)
print(count)