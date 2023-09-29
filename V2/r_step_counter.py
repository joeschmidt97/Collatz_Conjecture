import csv


def odd_int_check(x):
    # check if given input is an odd integer, if not return an error
    if x % 2 != 0 and isinstance(x,int):
        pass
    else:
        raise ValueError(f'The number given {x} must be an odd integer.')


def count_r_steps(q, n):
    odd_int_check(q) #check if variable is an odd integer
    odd_int_check(n) #check if variable is an odd integer

    r_count = 0
    n = q * n + 1 #perform odd operation
        
    # perform even operations and keep count
    while n % 2 == 0: 
        n /= 2
        r_count += 1
        
    return r_count


### WRITE r-families by seeding odd int taking r-steps, explore +/- 2^(r+1) , and adding modulo class for skipping checks ################



def write_r_families_MODULO(q:int, r_count_i:int, r_count_f:int, r_len_cutoff:int = 20):

    r_dict = {}
    n = 1

    while set(range(r_count_i, r_count_f + 1)) - set(r_dict.keys()):

        skip_r_family_build = False #reset skip block boolean

        for r_key in r_dict:
            r_family_dict = r_dict[r_key]
            odd_in_r_family_check = check_in_modulo_family(n, r_family_dict)

            if odd_in_r_family_check:
                # print(n, r_modulo)
                skip_r_family_build = True  # Set the flag to skip the code block
                break  # Exit the for loop

        if not skip_r_family_build:
            r_count, r_family = complete_r_family(q, n, r_len_cutoff)

            modulo = make_modulo_r_family(r_count, r_family)
            r_dict[r_count] = {'modulo': modulo, 'r_family': r_family}

            # Sort the r-families by increasing r-value
            r_dict = dict(sorted(r_dict.items()))

        n += 2
    
    # This cuts the unneeded r-values from dict
    # The cut is done here so the code can use the modulo skip on every number and save compute 
    # (i.e. we keep r=1 (1,8) even if r_count_i > 1 so that all numbers of form 1+8m are not computed but skipped)
    r_dict_cut = {r_key: r_family_dict for r_key, r_family_dict in r_dict.items() 
                  if r_count_i <= r_key <= r_count_f}

    return r_dict_cut


def complete_r_family(q:int, n_i:int, r_len_cutoff:int=10):

    r_family = [n_i]

    odd_int_check(n_i) #check if variable is an odd integer
    r_count_i = count_r_steps(q, n_i) # get r vale

    n = n_i
    while len(r_family) < r_len_cutoff:

        if r_family[0] - 2**(r_count_i+1) > 0:
            n -= 2**(r_count_i+1)
        else:
            n = r_family[-1] + 2**(r_count_i+1)

        r_count = count_r_steps(q, n)

        if r_count != r_count_i:
            raise ValueError(f'The resulting odd {n} is not part of the step-family {r_count_i}')
        
        r_family.append(n)
        r_family.sort()
    
    if r_family[0] - 2**(r_count_i+1) > 0:
        print(f'The smallest odd integer for r={r_count_i} was not found. Try a smaller initial odd ({n_i}) or a larger cutoff length ({r_len_cutoff}).')

    return r_count, r_family




def make_modulo_r_family(r_count:int, r_family:list):

    differences = []

    for i in range(len(r_family) - 1):
        diff = r_family[i + 1] - r_family[i]
        differences.append(diff)

    # Check if all elements in the list are the same
    all_elements_same = all(x == differences[0] for x in differences)

    if not all_elements_same:
        raise ValueError("Not all elements in 'differences' are the same.")

    remainder = differences[0]

    if r_family[0] - remainder > 0:
        print(f'The smallest odd integer for the r={r_count} family was not found. Try reloading your r-family to include an integer such that {r_family[0]} < {remainder}.')

    smallest_odd = r_family[0]

    return (smallest_odd, remainder)



def check_in_modulo_family(n_check:int, r_family_dict:dict):

    smallest_odd, remainder = r_family_dict['modulo']

    # smallest_odd, remainder = modulo_tuple

    if (n_check - smallest_odd) % remainder == 0:
        in_r_family = True
    else:
        in_r_family = False

    return in_r_family



################## WRITE and READ r-families to CSV  ########################


def write_r_dict_to_CSV(r_dict):
    
    filename = f"DATA/q={r_dict['q']}_r_data.csv"

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(['q', r_dict['q']])
        # Write the header row
        writer.writerow(['r', 'modulo', 'len_odds', 'odds'])

        # Iterate over the data and write rows
        for r_step, r_family_dict in r_dict.items():
            if isinstance(r_step, int):
                row = [r_step, r_family_dict['modulo'], len(r_family_dict['r_family'])] +  r_family_dict['r_family']
                writer.writerow(row)


def read_CSV_to_r_dict(filename):
    r_dict = {}
    
    with open(filename, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        
        if header[0] != 'q':
            raise ValueError("Invalid CSV format. The first row should start with 'q'.")
        
        r_dict_values = {}
        
        for row in reader:
            if row[0] == 'q':
                r_dict['q'] = int(row[1])
            else:
                try: 
                    r_step = int(row[0])
                    modulo = eval(row[1])  # Use eval to convert the string "(1, 4)" to a tuple
                    r_family = [int(value) for value in row[3:]]  # Convert remaining values to integers
                
                    r_dict_values[r_step] = {'modulo': modulo, 'r_family': r_family}
                except:
                    pass

        r_dict.update(r_dict_values)
    
    return r_dict









### WRITE r-families by going through odds one by one ##################

def write_r_families_ITERATIVE(q, int_i, int_f, r_cutoff=float('inf')):

    odd_int_check(int_i) #check if variable is an odd integer

    r_families = {}

    # create list of odd integers to get r-steps
    for n in range(int_i, int_f, 2):
        r_count = count_r_steps(q, n) # get r vale

        # Check if the key exists in r_families, and create it if it doesn't
        if r_count not in r_families:
            r_families[r_count] = []

        # Only add the odd to its r-family if there is space (i.e. r-family is below cutoff length)
        if len(r_families[r_count]) < r_cutoff:
            r_families[r_count].append(n)

    # Sort the r-families by increasing r-value
    sorted_r_families = dict(sorted(r_families.items()))

    return sorted_r_families


def r_dict_to_csv(r_dict):
    # Create a CSV file and write the data
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['q', r_dict['q']])
        writer.writerow(['len', 'r', 'odds'])
        for key, values in r_dict.items():

            if isinstance(key, int):
                writer.writerow([len(values), key] + values)
