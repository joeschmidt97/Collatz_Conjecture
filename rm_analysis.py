from rm_dict_builder import rm_dict_builder

q = 7
N = 3000001

r_m_dict = rm_dict_builder(q, N)
print(r_m_dict)

print(q,'n + 1')
for i,r in enumerate(r_m_dict['r']):
    
    r = r_m_dict['r'][i]
    odd = r_m_dict['base_odd'][i]
    m = r_m_dict['even_offset'][i]

    print('r:',r,'|', odd,'+', m,'m')
print('--------------------')

odd_list = r_m_dict['base_odd']
odd_diff_list = [odd_list[i+1] - odd_list[i] for i in range(len(odd_list)-1)]
mod_odd_diff = []

for i in range(len(odd_diff_list)):
    odd_diff = odd_diff_list[i]
    odd_diff_DIV = odd_diff_list[i]//(2**(i+1))

    mod_odd_diff.append(odd_diff_DIV)

    print('odd diff:', odd_diff, '| odd diff/2^r:',odd_diff_DIV)

print(mod_odd_diff)
# print(odd_diff_list)



print('--------------------------')
for q in range(3,29,2):
    # print(q)

    r_m_dict = rm_dict_builder(q, N)
    for i,r in enumerate(r_m_dict['r']):
        
        r = r_m_dict['r'][i]
        odd = r_m_dict['base_odd'][i]
        m = r_m_dict['even_offset'][i]

    
    odd_list = r_m_dict['base_odd']
    odd_diff_list = [odd_list[i+1] - odd_list[i] for i in range(len(odd_list)-1)]
    mod_odd_diff = []

    for i in range(len(odd_diff_list)):
        odd_diff = odd_diff_list[i]
        odd_diff_DIV = odd_diff_list[i]//(2**(i+1))

        mod_odd_diff.append(odd_diff_DIV)

    
    print(q, mod_odd_diff)
    # print(odd_diff_list)


