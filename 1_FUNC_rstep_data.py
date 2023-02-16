import csv
from FUNC_odd_to_odd import odd_to_odd_step_counter


def READ_rstep_from_CSV(filename):
    # print(filename)

    rstep_dict = {}
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)  # create a CSV reader object
        next(csvreader)         # skip the header row with column names

        # read the data rows and populate the dictionary
        for row in csvreader:
            key = row[0]
            values = [cell for cell in row[1:] if cell != ''] #read values if they are not empty
            int_values = [int(i) for i in values] #convert list of strings to int
            rstep_dict[key] = int_values

    return rstep_dict



def rstep_dict(q, n_min, n_max):
    from collections import defaultdict

    if n_min > 1:
        pass
    else:
        n_min = 1

    print(n_min)
    #Setup odds to extract r,m info from
    odd_range = range(n_min, n_max, 2)

    #Loop through odds and collect the r (steps) for each odd
    rstep_dict = defaultdict(list)
    for n in odd_range:
        odd_0, odd_1, steps = odd_to_odd_step_counter(n,q)
        rstep_dict[steps].append(odd_0)

    rstep_dict = dict(sorted(rstep_dict.items())) #sort r (step) dict numerically

    return rstep_dict



def rstep_data_generator(q, n_max):
    import os

    #Check to see if there is already data in a CSV and extract it
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
    os.chdir(data_path)
    filename = 'q=' + str(q) + '_r_step_data.csv' #change file depending on q value
    rstep_CSV_exists = os.path.exists(filename)

    if rstep_CSV_exists:
        rstep_dict = READ_rstep_from_CSV(filename)

        # Find largest odd tested in CSV file
        n_max_dict = 0  # Initialize to 0
        for key, value in rstep_dict.items():
            print(value)
            n_max_dict = max(n_max_dict, max(value)) #update to find max value
    
    
        print(rstep_dict)
        print(n_max_dict)
        # return rstep_dict, n_max_dict
    else:
        print('no file found for q=', q)
    
    
    return





q = 3
n_min = 3
n_max = 100

rstep_dict = rstep_dict(q, n_min, n_max)
# print(rstep_dict)

# rstep_data_generator(q, n_max)