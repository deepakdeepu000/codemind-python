n=int(input())
a=list(map(int,input().split()))
result = 0
for digits in a:
    result = (result << 1) | digits
print ( str(result))