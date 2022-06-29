n = int(input())
a = len(str(n))
b=n
k=0
while b > 0:
    c = b % 10
    k = k + int(c**a)
    b = b // 10
    a = a - 1


if k == n:
    print("True")
else:
    print("False")