
def odd_int_check(x):
    # check if given input is an odd integer, if not return an error
    if x % 2 != 0 and isinstance(x,int):
        pass
    else:
        raise ValueError(f'The number given {x} must be an odd integer.')


def count_r_steps(q, n):
    odd_int_check(q) #check if variable is an odd integer
    odd_int_check(n) #check if variable is an odd integer

    r_count = 0
    n = q * n + 1 #perform odd operation
        
    # perform even operations and keep count
    while n % 2 == 0: 
        n /= 2
        r_count += 1
        
    return r_count

