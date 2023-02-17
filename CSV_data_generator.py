from FUNC_rstep_data import WRITE_rstep_to_CSV
from FUNC_rm_data import WRITE_rm_to_CSV

def WRITE_rstep_rm_CSV(q, n_max):
    WRITE_rstep_to_CSV(q, n_max)
    WRITE_rm_to_CSV(q) 

n_max = 1000000001
# q_range = range(1,51,2)
q_range = [11,13,17,19,23,25,27,29,33,35,37,39,41,43,45,47,49,51]
for q in q_range:
    print(q)
    WRITE_rstep_rm_CSV(q, n_max)



# x_range = [9,10]
# for x in x_range:
#     q = 2**x - 1
#     print('q=',q)
#     WRITE_rstep_rm_CSV(q, n_max)