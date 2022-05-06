a=int(input())
import math
b= math.sqrt(a)
c=0
for i in range(1,a):
    if i*i==a:
        c=i
if c==b:
    print("True")
else:
    print("False")
    