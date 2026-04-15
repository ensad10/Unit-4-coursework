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

# --- Section 1: LOADING 
    with open(filename, 'r') as file:
        for line in file:
            items = line.strip().split(',')
            
            if len(items) == 7:
                record = {
                    "V_ID": items[0],
                    "V_Name": items[1],
                    "Year_and_week": items[2],
                    "Veg_dogs_sold": items[3],
                    "Meat_dogs_sold": items[4],
                    "Onions": items[5],
                    "Ketchup_L": items[6],
                }
                final_data.append(record)
    return final_data
# --- Section 2: VALIDATING Begins here. 
def validate_data(records):
    valid_records = []

    for record in records:
        is_valid = True
        

