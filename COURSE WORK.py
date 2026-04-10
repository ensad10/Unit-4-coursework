# Vendor ID 
# Vendor name (Done)
# Year and Week 
# Number of vegan hotdogs (Done)
# Number of meat hotdogs (Done)
# Onions (Kg) (Done)
# Ketchup (Litres) (Done)

# START TIMER 
import time 
start = time.time() 

final_data = [] 
record_list = []

# section 1: LOADING 
with open('hotdogs.txt', 'r') as file:
  for line in file:
    items = line.strip().split(',')
    if len(items) < 7: continue # This skips any empty lines which are irrelivant

    record = {
        "V_ID": items[0],
        "V_Name: items": items[1],
        "Year_and_week": items[2],
        "Veg_dogs_sold": items[3],
        "Meat_dogs_sold": items[4],
        "Onions": items[5],
        "Kechtup_L": items[6],




    
