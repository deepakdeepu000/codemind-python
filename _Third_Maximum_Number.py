n=int(input())
a=list(map(int,input().split()))
f=sorted(list(set(a)))
print(f[len(f)-3])
