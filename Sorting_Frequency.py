from collections import *

def sort_array(m,n):
    F=defaultdict(lambda:0)
    for i in range(n):
        F[m[i]]+=1
    m.sort(key=lambda x:(-F[x],x))
    return m

n=int(input())
list1=list(map(int,input().split()))
t=sort_array(list1,n)

for T in sorted(set(t),key=t.index):
    print(T,end=' ')