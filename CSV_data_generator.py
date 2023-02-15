import sys

filepath_git = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture'
# sys.path.append('C:\\Users\\joesc\\git\\Collatz_Conjecture\\Collatz_Conjecture\\functions')
sys.path.append(filepath_git + '/functions')
from rm_to_CSV import WRITE_r_step_to_CSV

filepath = filepath_git + '/DATA'

q = 5
n_max = 101
WRITE_r_step_to_CSV(q, n_max, filepath)
# rm_to_CSV.WRITE_rm_dict_to_CSV(q, n_max)
