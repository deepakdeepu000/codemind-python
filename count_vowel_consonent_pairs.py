n=input()
l=len(n)
l=l//2
m=0
a='aeiou'
k=1
for i in range(0,l):
    if n[i] in a and n[-k] not in a and n[-k]!=" " or n[i] not in a and n[0-k] in a and n[i]!=" ": 
        m+=1
    k+=1
print(m)
    
    