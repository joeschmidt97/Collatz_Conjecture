import os
import csv
from FUNC_odd_to_odd import odd_to_odd_step_counter


def READ_rstep_from_CSV(q):
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
    os.chdir(data_path)
    filename = 'q='+ str(q) + '_rstep_data.csv'
    rstep_CSV_exists = os.path.exists(filename)

    if rstep_CSV_exists:
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
    else:
        print('No file for q=',q, 'exists. Creating one now for odds from 1-1001')        
        rstep_dict = rstep_dict_builder(q, 1, 1001)
        WRITE_rstep_to_CSV(q, 1001)
        rstep_dict = {}

        return rstep_dict


def WRITE_rstep_to_CSV(q, n_max):
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
    os.chdir(data_path)
    filename = 'q='+ str(q) + '_rstep_data.csv'

    rstep_dict = rstep_data_aggragator(q, n_max)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile) # create a CSV writer object

        # get the maximum length of the values in the dictionary
        max_len = min(max(len(values) for values in rstep_dict.values()), 100) #limit the max length of column printouts to 100
        col_labels = ['r'] + [f'm={i}' for i in range(max_len)] # create a list of column labels
        writer.writerow(col_labels)         # write the header row with column names

        # write the data rows with values and empty cells as needed
        for key, values in rstep_dict.items():
            row = [key] + values[:max_len] + [''] * (max_len - len(values))
            writer.writerow(row)

    return


def rstep_dict_builder(q, n_min, n_max):
    from collections import defaultdict

    #set minimum odd value to test
    if n_min > 1:
        pass
    else:
        n_min = 1

    #Setup odds to extract r,m info from
    odd_range = range(n_min, n_max, 2)
    
    #Loop through odds and collect the r (steps) for each odd
    rstep_dict = defaultdict(list)
    for n in odd_range:
        # print(n)
        odd_0, odd_1, steps = odd_to_odd_step_counter(n,q)
        rstep_dict[str(steps)].append(odd_0) #add odd to r family and make sure step is a string value

    rstep_dict = dict(sorted(rstep_dict.items())) #sort r (step) dict numerically
    return rstep_dict



def append_dict_data(q, rstep_dict1, n_max_dict1, n_max):
    if n_max_dict1 < n_max:
        print('CSV file for q=', q, 'tested up to', n_max_dict1, '~Generating data up to', n_max)

        rstep_dict2 = rstep_dict_builder(q, n_max_dict1, n_max)
        
        for key, value in rstep_dict2.items():
            if key in rstep_dict1:
                # Use a set to keep track of unique values in d1
                unique_values = set(rstep_dict1[key])
                for v in value:
                    # Check if v is already in the set, and append if not
                    if v not in unique_values:
                        rstep_dict1[key].append(v)
                        unique_values.add(v)
            else:
                rstep_dict1[key] = value
    else:
        print('CSV file for q=', q, 'tested up to', n_max_dict1, 'already (Upper bound given as ', n_max,'). No more data to save to CSV.')
        pass

    return rstep_dict1


def rstep_data_aggragator(q, n_max):
   
    #Check to see if there is already data in a CSV and extract it
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
    os.chdir(data_path)
    filename = 'q=' + str(q) + '_rstep_data.csv' #change file depending on q value
    rstep_CSV_exists = os.path.exists(filename)

    if rstep_CSV_exists:
        rstep_dict1 = READ_rstep_from_CSV(q)

        # Find largest odd tested in CSV file
        n_max_dict1 = 0  # Initialize to 0
        for key, value in rstep_dict1.items():
            n_max_dict1 = max(n_max_dict1, max(value)) #update to find max value
        
        rstep_dict = append_dict_data(q, rstep_dict1, n_max_dict1, n_max)
    else:
        print('No CSV file found for q=', q, '~Generating data now.')
        n_min = 1
        rstep_dict = rstep_dict_builder(q, n_min, n_max)


    rstep_dict = dict(sorted(rstep_dict.items(), key=lambda x: int(x[0]))) #sort r (step) dict numerically

    return rstep_dict

