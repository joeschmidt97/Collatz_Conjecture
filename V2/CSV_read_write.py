import csv


# Open the CSV file for writing
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
