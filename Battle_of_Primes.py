def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    else:
        return 1
a=int(input())
b=int(input())
c=a+b
for i in range(1,100):
    if prime(c+i):
        print(i)
        break