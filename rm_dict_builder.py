from statistics import mode
from collections import defaultdict
from odd_to_odd_func import odd_to_odd_step_counter

q = 5
N = 30001

#Setup odds to extract r,m info from
odd_range = range(1, N, 2)

#Loop through odds and collect the r (steps) for each odd
step_dict = defaultdict(list)
for n in odd_range:
    odd_0, odd_1, steps = odd_to_odd_step_counter(n,q)
    step_dict[steps].append(odd_0)

step_dict = dict(sorted(step_dict.items())) #sort r (step) dict numerically

#Assume we can write out every odd number as: base_odd + even_offset*m
#Exract out the even_offset from the list of all odds in a r (step) family
r_m_dict = defaultdict(list)
for r in step_dict:
    r_odds = step_dict[r] #all odds in an r (step) family

    diff_list = [r_odds[i+1] - r_odds[i] for i in range(len(r_odds)-1)] #compute the difference between odds in an r (step) family

    if diff_list:
        base_odd = r_odds[0] #This is the base odd
        even_offset = mode(diff_list) #Get the even_offset as the most likely difference between odds

        #Add r, base_odd, and even_offset as lists to a dict
        r_m_dict['r'].append(r)
        r_m_dict['base_odd'].append(base_odd)
        r_m_dict['even_offset'].append(even_offset)


print(r_m_dict)

print(q,'n + 1')
for i,r in enumerate(r_m_dict['r']):
    
    r = r_m_dict['r'][i]
    odd = r_m_dict['base_odd'][i]
    m = r_m_dict['even_offset'][i]

    print('r:',r,'|', odd,'+', m,'m')

odd_list = r_m_dict['base_odd']
odd_diff_list = [odd_list[i+1] - odd_list[i] for i in range(len(odd_list)-1)]

print(odd_diff_list)

