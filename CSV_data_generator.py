import sys
from FUNC_rm_to_CSV import WRITE_r_step_to_CSV, WRITE_rm_dict_to_CSV

filepath_git = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture'
filepath = filepath_git + '/DATA'

q = 13
n_max = 70000001
print('Producing data for q=',q)
WRITE_r_step_to_CSV(q, n_max, filepath)
WRITE_rm_dict_to_CSV(q, n_max, filepath)
