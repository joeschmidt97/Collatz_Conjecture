from odd_to_odd_func import odd_to_odd_step_counter

q = 3
n = 301

odd_0, odd_1, steps = odd_to_odd_step_counter(n,q)

print(odd_0, odd_1)
print('steps:', steps)