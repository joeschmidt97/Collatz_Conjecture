from A_FUNC_rstep_data import WRITE_rstep_to_CSV
from A_FUNC_rm_data import WRITE_rm_to_CSV
# filepath_git = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture'
# filepath = filepath_git + '/DATA'
#511



q = 7
n_max = 100001
WRITE_rstep_to_CSV(q, n_max)
WRITE_rm_to_CSV(q)
# WRITE_r_step_to_CSV(q, n_max, filepath)
# WRITE_rm_dict_to_CSV(q, n_max, filepath)
