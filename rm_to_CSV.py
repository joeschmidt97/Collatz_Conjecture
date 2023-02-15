import csv
from rm_dict_builder import rm_dict_builder


def r_step_dict_to_CSV(q, n_max):
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



def rm_dict_to_CSV(q, n_max):
    rm_dict, r_step_dict = rm_dict_builder(q, n_max)

    filename = str(q) + 'n_plus_1_rm_data.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(rm_dict.keys())
        writer.writerows(zip(*rm_dict.values()))



q = 3
n_max = 100003
rm_dict_to_CSV(q, n_max)
r_step_dict_to_CSV(q, n_max)
