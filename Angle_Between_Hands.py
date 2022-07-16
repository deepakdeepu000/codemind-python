a,b=map(int,input().split(':'))
c=abs(30*a-((11/2)*b))
d=360-c
if c<d:
    print(c)
else:
    print(d)