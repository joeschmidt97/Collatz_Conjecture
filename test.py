# Comment thing

q = 3
n = 4

def odd_operation(n, q):
    odd_step = int(q*n + 1)
    return odd_step

def even_operation(n):
    even_step = int(n/2)
    return even_step

def odd_even_operation(n, q):
    if (n%2 == 0): #divisible by 2, or even
        N = even_operation(n)
    else:
        N = odd_operation(n,q)
    return N


N = odd_even_operation(n, q)
print(n,">", N)

