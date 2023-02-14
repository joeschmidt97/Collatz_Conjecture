import csv
from rm_dict_builder import rm_dict_builder


def r_step_dict_to_CSV(q, n_max):

    rm_dict, r_step_dict = rm_dict_builder(q, n_max)

    filename = str(q) + 'n_plus_1_r_step_data.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(rm_dict.keys())
        writer.writerows(zip(*rm_dict.values()))




def rm_dict_to_CSV(q, n_max):
    
    rm_dict, r_step_dict = rm_dict_builder(q, n_max)

    filename = str(q) + 'n_plus_1_rm_data.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(rm_dict.keys())
        writer.writerows(zip(*rm_dict.values()))




q = 7
n_max = 1000003
rm_dict_to_CSV(q, n_max)
r_step_dict_to_CSV(q, n_max)
