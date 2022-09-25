def reversevowels(s):
    c = list(s)
    x = []
    v = []
    for i in range(len(c)):
        if c[i] in ['a','e','i','o','u','A','E','I','O','U']:
         v.append(c[i])
         x.append(i)
    v =v[::-1]
    f = []
    ind = 0
    for i in range(len(c)):
        if i in x:
            f.append(v[ind])
            ind += 1
        else:
            f.append(c[i])
    str1 = ""
    return str1.join(f)
n=input()
print(reversevowels(n))