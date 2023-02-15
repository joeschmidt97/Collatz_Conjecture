import sys
# sys.path.append('C:\\Users\\joesc\\git\\Collatz_Conjecture\\Collatz_Conjecture\\functions')
sys.path.append('C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/functions')
import rm_to_CSV

q = 3
n_max = 10000001
rm_to_CSV.WRITE_r_step_to_CSV(q, n_max)
rm_to_CSV.WRITE_rm_dict_to_CSV(q, n_max)
