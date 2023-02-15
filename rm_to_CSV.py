import csv
from rm_dict_builder import rm_dict_builder


# R-step data to/from CSV 


def WRITE_r_step_to_CSV(q, n_max):
    rm_dict, r_step_dict = rm_dict_builder(q, n_max)

    filename = str(q) + 'n_plus_1_r_step_data.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile) # create a CSV writer object

        # get the maximum length of the values in the dictionary
        max_len = min(max(len(values) for values in r_step_dict.values()), 100) #limit the max length of column printouts to 100
        col_labels = ['r'] + [f'm={i}' for i in range(max_len)] # create a list of column labels
        writer.writerow(col_labels)         # write the header row with column names

        # write the data rows with values and empty cells as needed
        for key, values in r_step_dict.items():
            row = [key] + values[:max_len] + [''] * (max_len - len(values))
            writer.writerow(row)


def READ_r_step_from_CSV(filename):
    r_step_dict = {}

    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)  # create a CSV reader object
        next(csvreader)         # skip the header row with column names

        # read the data rows and populate the dictionary
        for row in csvreader:
            key = row[0]
            values = [cell for cell in row[1:] if cell != ''] #read values if they are not empty
            r_step_dict[key] = values

    return r_step_dict




# RM data to/from CSV 

def WRITE_rm_dict_to_CSV(q, n_max):
    rm_dict, r_step_dict = rm_dict_builder(q, n_max)
    print(rm_dict)

    filename = str(q) + 'n_plus_1_rm_data.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(rm_dict.keys())
        writer.writerows(zip(*rm_dict.values()))



def READ_rm_dict_to_CSV(filename):
    rm_dict = {}

    with open(filename) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=',')

        # Read the header row and create a key in the dictionary for each column
        header = next(csvreader)
        for i in range(len(header)):
            rm_dict[header[i]] = []

        # Loop through each row in the CSV and add the non-empty values to the dictionary
        for row in csvreader:
            for i in range(len(header)):
                if row[i]: # Check whether the cell is non-empty
                    rm_dict[header[i]].append(int(row[i])) # Add the value to the list associated with the key

    return rm_dict









q = 3
n_max = 100003
# WRITE_r_step_to_CSV(q, n_max)
# WRITE_rm_dict_to_CSV(q, n_max)
# r_step_dict = READ_r_step_from_CSV('3n_plus_1_r_step_data.csv')

rm_dict = READ_rm_dict_to_CSV('3n_plus_1_rm_data.csv')
print(rm_dict)

