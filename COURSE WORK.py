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
        is_valid = True
        

