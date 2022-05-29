

def reverse(n):
    rev_n = 0
    while (n > 0):
        a=n%10
        rev_n = rev_n * 10 + a
        n = n//10
    return rev_n
  
def pal(n):
    return (reverse(n) == n)
def Rev_add(n):
    rev_n = 0
    while (n>0):
        rev_n = reverse(n)
        n = n + rev_n
        if(pal(n)):
            print (n)
            break
n=int(input())
Rev_add(n)
