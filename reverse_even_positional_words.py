def rev(n):
    a=n[::-1]
    return a

n=input()
n=n.split()
for i in range(len(n)):
    if i%2==0:
        print(rev(n[i]),end=" ")
    else:
        print(n[i],end=" ")