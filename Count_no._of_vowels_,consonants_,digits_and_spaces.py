s=input()
s1=s.lower()
c,s,k,r=0,0,0,0
for i in s1:
    if i in 'aeiou':
        c+=1
    elif i in 'bcdfghjklmnopqrstvwxyz':
        s+=1
    elif i is ' ':
        k+=1
    else:
        r+=1
print("Vowels:",c)
print("Consonants:",s)
print("Digits:",r)
print("White spaces:",k)