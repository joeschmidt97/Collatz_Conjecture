import os
import matplotlib.pyplot as plt
from FUNC_rm_to_CSV import READ_rm_dict_to_CSV


def q_analysis(q):
    path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
    os.chdir(path)
    filename = 'q=' + str(q) + '_rm_data.csv' #change file depending on q value

    r_m_dict = READ_rm_dict_to_CSV(filename)
    print(q,'n + 1')


    odd_list = r_m_dict['base_odd']
    odd_diff_list = [odd_list[i+1] - odd_list[i] for i in range(len(odd_list)-1)]
    mod_odd_diff = []

    for i in range(len(odd_diff_list)):
        odd_diff = odd_diff_list[i]
        odd_diff_DIV = odd_diff_list[i]//(2**(i+1))

        mod_odd_diff.append(odd_diff_DIV)
        # print('odd diff:', odd_diff, '| odd diff/2^r:',odd_diff_DIV)

    plt.figure()
    plt.title(q)
    plt.plot(r_m_dict['r'][:-1],mod_odd_diff, "-o")
    # Show/save figure as desired.
    plt.show()

    # print(r_m_dict['r'][:-1])
    # print(mod_odd_diff)
    # print(odd_diff_list)


q = 29
q_analysis(q)


M_prime_loop = False
if M_prime_loop:
    x_range = [1,2,3,4,5,6,7,8,9]
    for x in x_range:
        q = 2**x - 1

        print('x=',x)
        q_analysis(q)
        print('')