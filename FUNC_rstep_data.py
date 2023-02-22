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







# def WRITE_rstep_to_CSV(q, n_min, n_max):
#     data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
#     os.chdir(data_path)
#     filename = 'q='+ str(q) + '_rstep_data.csv'

#     rstep_dict = rstep_data_aggragator(q, n_min, n_max)

#     with open(filename, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile) # create a CSV writer object

#         # Find the smallest odd number in the dictionary
#         smallest_odd = min(filter(lambda x: x % 2 == 1, [elem for lst in rstep_dict.values() for elem in lst]))

#         # Determine the index of the smallest odd number in the row
#         row_labels = ['m=' + str(i) for i in range(0, -6, -1)] + ['m=' + str(i) for i in range(1, len(rstep_dict.values()) + 1)]
#         smallest_odd_index = row_labels.index('m=0')

#         # Find the maximum length of the column with the negative values to the left of the smallest odd number
#         max_len = min(max(len([elem for elem in lst if elem <= smallest_odd and elem % 2 == 1]) for lst in rstep_dict.values()), 100)

#         # Create the header row with modified labels
#         col_labels = ['r'] + row_labels
#         writer.writerow(col_labels)

#         # Write the data rows with values and empty cells as needed
#         for key, values in rstep_dict.items():
#             # Filter out negative values to the right of the smallest odd
#             filtered_values = [elem for elem in values if elem <= smallest_odd and elem % 2 == 1]
#             filtered_values.reverse()  # Reverse the list to align with the modified header row
#             # Get only the 5 negative values to the left of the smallest odd
#             negative_values = filtered_values[max(smallest_odd_index - 5, 0):smallest_odd_index]
#             positive_values = [elem for elem in values if elem > smallest_odd and elem % 2 == 1][:max_len-len(negative_values)]
#             row = [key] + negative_values + [''] * (smallest_odd_index - len(negative_values)) + positive_values + [''] * (max_len - len(negative_values) - len(positive_values))
#             writer.writerow(row)
#     return




def WRITE_rstep_to_CSV(q, n_min, n_max):
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
    os.chdir(data_path)
    filename = 'q='+ str(q) + '_rstep_data.csv'

    rstep_dict = rstep_data_aggragator(q, n_min, n_max)
    rstep_dict = rstep_dict_trimmer(rstep_dict)

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
    #Setup odds to extract r,m info from
    odd_range = range(n_min, n_max+2, 2)

    #Loop through odds and collect the r (steps) for each odd
    rstep_dict = defaultdict(list)
    for n in odd_range:
        odd_0, odd_1, steps = odd_to_odd_step_counter(n,q)
        rstep_dict[str(steps)].append(odd_0) #add odd to r family and make sure step is a string value

    rstep_dict = dict(sorted(rstep_dict.items())) #sort r (step) dict numerically
    return rstep_dict



def merge_dict(dict_OG, dict1):
    for key, value in dict1.items():
        if key in dict_OG:
            # Use a set to keep track of unique values
            unique_values = set(dict_OG[key])
            for v in value:
                # Check if v is already in the set, and append if not
                if v not in unique_values:
                    dict_OG[key].append(v)
                    unique_values.add(v)
            dict_OG[key] = sorted(dict_OG[key]) #sorts values numerically
        else:
            dict_OG[key] = sorted(value)
        
    return dict_OG


def append_dict_data(q, rstep_dict1, n_min, n_max):
    # Find largest and smallest odd tested in CSV file
    n_max_dict1 = 0  # Initialize to 0
    n_min_dict1 = 0  # Initialize to 0
    for key, value in rstep_dict1.items():
        n_max_dict1 = max(n_max_dict1, max(value)) #update to find max value
        n_min_dict1 = min(n_min_dict1, min(value)) #update to find min value
    
    lower_range = (n_min < n_min_dict1)
    upper_range = (n_max > n_max_dict1)

    if lower_range or upper_range:
        print('CSV file for q=', q, 'testing from', n_min, 'to', n_max)

        if lower_range:
            rstep_dict_lower = rstep_dict_builder(q, n_min, n_min_dict1)
            rstep_dict1 = merge_dict(rstep_dict1, rstep_dict_lower)

        if upper_range:
            rstep_dict_upper = rstep_dict_builder(q, n_max_dict1, n_max)
            rstep_dict1 = merge_dict(rstep_dict1, rstep_dict_upper)
 
    else:
        print('CSV file for q=', q, 'tested from', n_min_dict1, 'to' ,n_max_dict1 ,'already. No more data to save to CSV.')
        pass

    return rstep_dict1


def rstep_data_aggragator(q, n_min, n_max):
   
    #Check to see if there is already data in a CSV and extract it
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'
    os.chdir(data_path)
    filename = 'q=' + str(q) + '_rstep_data.csv' #change file depending on q value
    rstep_CSV_exists = os.path.exists(filename)

    if rstep_CSV_exists:
        rstep_dict1 = READ_rstep_from_CSV(q)
        rstep_dict = append_dict_data(q, rstep_dict1, n_min, n_max)
    else:
        print('No CSV file found for q=', q, '~Generating data now from', n_min, 'to', n_max)
        rstep_dict = rstep_dict_builder(q, n_min, n_max)

    rstep_dict = dict(sorted(rstep_dict.items(), key=lambda x: int(x[0]))) #sort r (step) dict numerically

    return rstep_dict

def rstep_dict_trimmer(rstep_dict):
    rstep_dict_trimmed = {}
    for key, value in rstep_dict.items():
        pos_values = [v for v in value if v > 0]
        if pos_values:
            rstep_dict_trimmed[key] = pos_values
    return rstep_dict_trimmed

