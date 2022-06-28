def sum_of_arr(lst):
    sum = 0
    for i in lst:
        if i % 2 != 0:
            sum = sum + i
        else: 
            break
    return sum

n=int(input())
a=list(map(int,input().split()))
print(sum_of_arr(a))