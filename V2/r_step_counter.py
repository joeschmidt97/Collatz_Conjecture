
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


def write_r_families(q, int_i, int_f, r_cutoff=float('inf')):

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



import csv

def r_dict_to_csv(r_dict):
    # Create a CSV file and write the data
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['q', r_dict['q']])
        writer.writerow(['odd_count', 'r', 'odds'])
        for key, values in r_dict.items():

            if isinstance(key, int):
                writer.writerow([len(values), key] + values)
