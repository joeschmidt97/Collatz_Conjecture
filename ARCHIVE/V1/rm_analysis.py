import matplotlib.pyplot as plt
from FUNC_rm_data import READ_rm_from_CSV


def q_analysis(q):
    rm_dict = READ_rm_from_CSV(q)
    print(q,'n + 1')

    odd_list = rm_dict['base_odd']
    odd_diff_list = [odd_list[i+1] - odd_list[i] for i in range(len(odd_list)-1)]
    mod_odd_diff = []

    for i in range(len(odd_diff_list)):
        odd_diff_DIV = odd_diff_list[i]//(2**(i+1))
        mod_odd_diff.append(odd_diff_DIV)

    plt.figure()
    plt.title(q)
    plt.plot(rm_dict['r'][:-1],mod_odd_diff, "-o")
    plt.show()



# q_range = range(1,51,2)
# for q in q_range:
#     print(q)
#     q_analysis(q)

#Expand 11,13,17,19,23,25,27,29,33,35,37,39,41,43,45,47,49


# q = 31
# q_analysis(q)


M_prime_loop = True
if M_prime_loop:
    x_range = [1,2,3,4,5,6,7,8,9,10]
    for x in x_range:
        q = 2**x - 1

        print('x=',x)
        q_analysis(q)
        print('')

