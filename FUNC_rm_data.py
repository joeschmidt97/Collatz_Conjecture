import csv
import os
from statistics import mode
from collections import defaultdict
from FUNC_rstep_data import READ_rstep_from_CSV

def rm_dict_builder(q):
    rstep_dict = READ_rstep_from_CSV(q)
    
    #Assume we can write out every odd number as: base_odd + even_offset*m
    #Exract out the even_offset from the list of all odds in a r (step) family
    rm_dict = defaultdict(list)
    for r in rstep_dict:
        r_odds = rstep_dict[r] #all odds in an r (step) family

        diff_list = [r_odds[i+1] - r_odds[i] for i in range(len(r_odds)-1)] #compute the difference between odds in an r (step) family

        if diff_list:
            base_odd = r_odds[0] #This is the base odd
            even_offset = mode(diff_list) #Get the even_offset as the most likely difference between odds

            #Add r, base_odd, and even_offset as lists to a dict
            rm_dict['r'].append(r)
            rm_dict['base_odd'].append(base_odd)
            rm_dict['odds_diff'].append(even_offset)

    rm_dict = dict(rm_dict) #Convert rm_dict list to dictionary

    return rm_dict


def WRITE_rm_to_CSV(q):
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'    
    os.chdir(data_path)
    filename = 'q='+ str(q) + '_rm_data.csv'

    rm_dict = rm_dict_builder(q)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(rm_dict.keys())
        writer.writerows(zip(*rm_dict.values()))

    return



def READ_rm_from_CSV(q):
    data_path = 'C:/Users/joesc/git/Collatz_Conjecture/Collatz_Conjecture/DATA'    
    os.chdir(data_path)
    filename = 'q='+ str(q) + '_rm_data.csv'

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

