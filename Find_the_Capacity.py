a,b,c=map(int,input().split())
s=2*a*b*c*512
c=s//1024
print("{0}KB".format(c))