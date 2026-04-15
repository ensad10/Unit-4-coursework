# Vendor ID 
# Vendor name (Done)
# Year and Week 
# Number of vegan hotdogs (Done)
# Number of meat hotdogs (Done)
# Onions (Kg) (Done)
# Ketchup (Litres) (Done)

# START TIMER 
import time 
# Loading my data Starts here. 
def load_data(filename):
    final_data = [] 
    record_list = []
# I made 2 empty lists in order to store the processed records and final_data after splitting the data into sections with (',')
    
# --- Section 1: LOADING 
# I open the file in read mode using a 'with' block to make sure the file is also closed 
# automatically after its processed, this stop memory from leaking.
    with open(filename, 'r') as file: 
# The strip() takes away the whitespaces for e.g (\n newlines)
# split (',') breaks each comma seperated string into a list of many items. 
        for line in file:
            items = line.strip().split(',')
# This checks the datas integrity by making sure the line has exactly 7 columns.
# it also acts as a safeguard towards the code crashing if there is a corrupt or empyty line.
            if len(items) == 7:
# I created a dictionary for the current record. 
# This is important because it specificly applying headers to the data values for better radibility 
                record = {
                    "V_ID": items[0],
                    "V_Name": items[1],
                    "Year_and_week": items[2],
                    "Veg_dogs_sold": items[3],
                    "Meat_dogs_sold": items[4],
                    "Onions": items[5],
                    "Ketchup_L": items[6],
                }
# This adds the completed dictionary to the main data list in this case (final_data)
                final_data.append(record)
    return final_data
# --- Section 2: VALIDATING Begins here. 
def validate_data(records):
# This is a list too ONLY hold the data that passes the validation checks 
    valid_records = []
    
    for record in records:
# Boolean is used here which remains True unless the validation has been violated 
        is_valid = True
# * FORMAT CHECKER - VENDOR ID *
# This validation checks if the VENDOR ID follows the required pattern: AA_123 etc. 
        v_id = record["V_ID"]
        if len(v_id) != 6 or not v_id[:2].isalpha() or not v_id[:2].isupper() or v_id[2] != '_' or not v_id[3:].isdigit():
            print(f"Invalid! Vendor ID '{v_id}' must be two uppercase letters, an underscore, and three digits.")
            is_valid = False
            
# * LENGTH CHECKER - VENDORS NAME *
# This validation checks if the names are practical for data entry for e.g (between 2-25 characters)
        if len(record["V_Name"]) < 2 or len(record["V_Name"]) > 25:
            print(f"Invalid! Vendor {record['V_ID']} name is too short or long.")
            is_valid = False
        
# * FORMAT & RANGE CHECKER - YEAR AND WEEK  *
# This validation checks the length of the date, it also makes sure to follow the format (YYYYWW) With a range of (1-52) weeks. 
        year_week = record["Year_and_week"]
        if len(year_week) != 6 or not year_week.isdigit():
            print(f"Invalid! Vendor {record['V_ID']} year and week must be in format YYYYWW.")
            is_valid = False
        else:
            week_number = int(year_week[4:])
            if week_number < 1 or week_number > 52:
                print(f"Invalid! Vendor {record['V_ID']} week number must be between 1 and 52.")
                is_valid = False
                
# * DATA TEST CHECKER - HOTDOG SALES *
# This validation uses the modulo operator % to make sure that it is in the multiples of 10. 
        if float(record["Veg_dogs_sold"]) % 10 != 0:
            print(f"Invalid! Vendor {record['V_ID']} veg hotdog sales must be divisible by 10.")
            is_valid = False

        if float(record["Meat_dogs_sold"]) % 10 != 0:
            print(f"Invalid! Vendor {record['V_ID']} meat hotdog sales must be divisible by 10.")
            is_valid = False

# * RANGE CHECKER - ONIONS *
# This validation Multiplies the data by 2 checking if it is a whole number this validates if the data is in (0.5 increments).
        onions = float(record["Onions"])
        if (onions * 2) % 1 != 0:
            print(f"Invalid! Vendor {record['V_ID']} onions must be in half kilogram increments.")
            is_valid = False
            
# * RNAGE CHECKER - KETCHUP *
# This validation stops the inputs at a reasonable range for e.g (1-4L). 
        if int(record["Ketchup_L"]) < 1 or int(record["Ketchup_L"]) > 4:
            print(f"Invalid! Vendor {record['V_ID']} ketchup must be between 1 and 4 litres.")
            is_valid = False
            
# * FINAL FILTERING *
# This makes sure that any record that remains True after the (is_valid) boolean is added to the valid_reord bank.
        if is_valid:
            valid_records.append(record)
# this line of code outputs a summary of how many valid records pass the cleaning proccess. 
    print(f"\nThere are {len(valid_records)} valid records\nOut of {len(records)} in total.")
    return valid_records

