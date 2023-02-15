import sys
# sys.path.append('C:\\Users\\joesc\\git\\Collatz_Conjecture\\Collatz_Conjecture\\functions')
sys.path.append('C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/functions')
import rm_to_CSV

q = 9
n_max = 103
rm_to_CSV.WRITE_r_step_to_CSV(q, n_max)
rm_to_CSV.WRITE_rm_dict_to_CSV(q, n_max)
