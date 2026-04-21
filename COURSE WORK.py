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

#~~~~~
# Loading DATA
#~~~~~
records = load_data('Hotdogs.txt')
records = validate_data(records)

#~~~~~
# MY MENU
#~~~~~

search_choice = int(input("What search Would you like to do? (1-3)\n1) Linear serach (sorted)\n2) Linear search (unsorted)\n3) Binary search\n\n"))
while search_choice > 3 or search_choice < 1:
    print("Invalid Value\n")
    search_choice = int(input("What search Would you like to do? (1-3)\n1) Linear serach (sorted)\n2) Linear search (unsorted)\n3) Binary search\n\n"))
if search_choice == 1:
    options = int(input("What do you want to linear search  (0-6)\n0) VendorID\n1) Vendor Name\n2) Year and week\n3) Veg hotdogs sold\n4) Meat hotdogs sold\n5) Onions\n6) Ketchup used\n\n~ "))


    while options > 6:
        print("Invalid Value\n")
        options = int(input("What do you want to linear search  (0-6)\n0) VendorID\n1) Vendor Name\n2) Year and week\n3) Veg hotdogs sold\n4) Meat hotdogs sold\n5) Onions\n6) Ketchup used\n\n~ "))
    if options > 2:
        higher_lower = int(input("Would you like to find the highest value or lowest value?\n\n(1) for highest\n(2) for lowest\n\n~ "))
        while higher_lower > 2:
            print("Invalid Value")
            higher_lower = int(input("Would you like to find the highest value or lowest value?\n\n(1) for highest\n(2) for lowest\n\n~ "))



