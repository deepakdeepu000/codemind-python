n=int(input())
a=n
b=0
while n!=0:
    c= n%10
    n=n//10
    b+=c
if a%b==0:
    print("True")
else:
    print("False")