import matplotlib.pyplot as plt
from rm_dict_builder import rm_dict_builder

q = 9
N = 30000001
all_odd_test = False


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

plt.figure()
plt.title(q)
plt.plot(r_m_dict['r'][:-1],mod_odd_diff, "-o")
# Show/save figure as desired.
plt.show()

print(r_m_dict['r'][:-1])
print(mod_odd_diff)
# print(odd_diff_list)



last_odd = 29
print('--------------------------')

if all_odd_test:
    for q in range(3,last_odd,2):
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
        
        plt.figure()
        plt.title(q)
        plt.plot(r_m_dict['r'][:-1],mod_odd_diff, "-o")
        # Show/save figure as desired.
    plt.show()


