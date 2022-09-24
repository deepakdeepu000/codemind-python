a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
alice=0
bob=0
if a>x:
    alice+=1
if a<x:
    bob+=1
if b>y:
    alice+=1
if b<y:
    bob+=1
if c>z:
    alice+=1
if c<z:
    bob+=1
print(alice,bob)
    