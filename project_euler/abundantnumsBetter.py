# not mine

def find_abundant(n):
    res = 1
    res += sum(sum((i, n // i))  for i in range(2, int(n**0.5) + 1) if n % i == 0)
    if int(n**0.5)**2 == n:
        res -= int(n**0.5)
    return res > n   

max_n =  28124 
list_n = list(range(1, max_n))
set_abundant = set(i for i in list_n if find_abundant(i))

res = 0
for value in range(1, max_n):
    for abundant in set_abundant:
        if abundant >= value:
            res += value
            break
        if (value - abundant) in set_abundant:
            break
print(res)