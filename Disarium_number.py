n = int(input())
l = len(str(n))

a = n
b = 0
r = 0

while a > 0:
    r= a % 10
    b = b + int(r**l)
    a = a // 10
    l = l - 1


if b == n:
    print("True")
else:
    print("False")