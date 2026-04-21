# START TIMER 
import time

#------------------
# LOAD MY DATA - changed from a dictionary to a list for efficency - 
#------------------

def load_data(filename):
    final_data = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                items = line.strip().split(',')
                final_data.append(items)
                    
    except:
        print("Could not find or read the file!")

    return final_data
#~~~~~
# VALIDATE DATA
#~~~~~

def validate_data(records):
    valid_records = []
    
    for record in records:
        # these lines of code check Vendor ID is uppercase, two letters, underscore, three digits e.g. AB_123
        if len(record[0]) != 6 or not record[0][:2].isupper() or not record[0][:2].isalpha() or record[0][2] != '_' or not record[0][3:].isdigit():
            continue
        
        # these lines of code check Vendor name is between 2 and 25 characters
        if len(record[1]) < 2 or len(record[1]) >25:
            continue

        # these lines of code check if the Year and Week is in format YYYYWW and week is between 1 and 52
        if len(record[2]) != 6 or not record[2].isdigit() or (int(record[2][3:]) >= 1 and int(record[2][3:]) <= 51): 
            continue
        
        # these lines of code check if the veg dogs sold are divisible by 10
        if int(record[3]) % 10 != 0:
            continue

        # these lines of code check if the meat dogs sold are divisible by 10
        if int(record[4]) % 10 != 0:
            continue
        # these lines of code check if the onions are in Increments of for e.g. 0.5, 1.0, 1.5
        if (float(record[5]) * 2).is_integer() == False:
            continue
        
        # these lines of code check if the ketchup is an integer between 1 and 4
        if int(record[6]) >= 1 and int(record[6]) <= 4:
            # Because everything else has passed the checks this record is ready to be added to valid_records list
            valid_records.append(record)


    print("~ After the validation check only", len(valid_records), "out of", len(records), "records have passed sucessfully ~\n")
    return valid_records


