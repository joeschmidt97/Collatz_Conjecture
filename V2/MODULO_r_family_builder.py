from CSV_read_write import read_CSV_to_r_dict
from r_step import odd_int_check, count_r_steps
from r_family_builder import check_in_modulo_family, complete_r_family, make_modulo_r_family

### WRITE r-families by seeding odd int taking r-steps, explore +/- 2^(r+1) , and adding modulo class for skipping checks ################

def smallest_r_family_odd(q:int, r:int):
    return ((2**r - 1)*q**(2**r - 1)) % 2**(r+1)


def write_r_families_MODULO(q:int, r_count_i:int, r_count_f:int, r_len_cutoff:int = 20):

    import os

    if os.path.exists(f'DATA/q={q}_r_data.csv'):
        filename = f'DATA/q={q}_r_data.csv'
        r_dict = read_CSV_to_r_dict(filename)

        r = list(r_dict.keys())[-1]
        n = smallest_r_family_odd(q, r + 1)
    else:
        r_dict = {}
        r = 1
        n = smallest_r_family_odd(q, r)

    while set(range(r_count_i, r_count_f + 1)) - set(r_dict.keys()):

        skip_r_family_build = False #reset skip block boolean

        for r_key in r_dict:
            r_family_dict = r_dict[r_key]
            odd_in_r_family_check = check_in_modulo_family(n, r_family_dict)

            if odd_in_r_family_check:
                # print(n, r_modulo)
                skip_r_family_build = True  # Set the flag to skip the code block
                break  # Exit the for loop
        
        # print(n, r, skip_r_family_build, len(r_dict))

        if not skip_r_family_build:
            r_count, r_family = complete_r_family(q, n, r_len_cutoff)

            modulo = make_modulo_r_family(r_count, r_family)
            r_dict[r_count] = {'modulo': modulo, 'r_family': r_family}

            # Sort the r-families by increasing r-value
            r_dict = dict(sorted(r_dict.items()))

            # print('n:', n, 'r:', r_count)
            # print(r_dict)

        r += 1
        n = smallest_r_family_odd(q, r)


    
    # This cuts the unneeded r-values from dict
    # The cut is done here so the code can use the modulo skip on every number and save compute 
    # (i.e. we keep r=1 (1,8) even if r_count_i > 1 so that all numbers of form 1+8m are not computed but skipped)
    r_dict_cut = {r_key: r_family_dict for r_key, r_family_dict in r_dict.items() 
                  if r_count_i <= r_key <= r_count_f}

    r_dict_cut['q'] = q

    return r_dict_cut




