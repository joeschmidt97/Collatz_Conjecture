

def odd_operation(n, q):
    b = 1
    # print('b=',b)
    odd_step = q*n + b
    return odd_step

def even_operation(n):
    even_step = n//2
    return even_step

def odd_to_odd_step_counter(n, q):
    if (n%2 == 0):
        print(n, 'is not an odd number')
        return
    else:
        odd_0 = n #store odd we start with
        steps = 0

        n = odd_operation(n,q) #first odd operation leading to an even
        while n%2 == 0: #apply even operations until reaching the next odd
            n = even_operation(n)
            steps += 1 #add a step count for every even operation
            
        odd_1 = n #store odd we end at

        return odd_0, odd_1, steps


