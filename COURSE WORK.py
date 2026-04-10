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

# --- Section 1: LOADING 
with open('hotdogs.txt', 'r') as file:
  for line in file:
    items = line.strip().split(',')
    if len(items) < 7: continue # This skips any empty lines which are irrelivant

    record = {
        "V_ID": items[0],
        "V_Name": items[1],
        "Year_and_week": items[2],
        "Veg_dogs_sold": items[3],
        "Meat_dogs_sold": items[4],
        "Onions": items[5],
        "Ketchup_L": items[6],
    }
    record_list.append(record)

# --- Section 2: VALIDATION
for i in record_list:
  is_valid = True
  v_id = i["V_ID"]

# Validation 1 
  if len(v_id) != 6 or not v_id[:2].isalpha() or not v_id[:2].isupper() or v_id[2] != '_' or not v_id[3:].isdigit():
    print(f"ERROR! Vendor ID '{v_id}' must be at least 2 uppercases, an underscore and three digits!")
    is_valid = False 

# Validation 2 
    if len(i["V_Name"]) < 2 or len(i["V_name"]) > 25:
      print(f"ERROR! Vendor {v_id}: Name is too short or long.")
      is_valid = False

# Validation 3
  year_week = i["Year_and_week"]
  if len(year_week) != 6 or not year_week.isdigit():
    print(f"ERROR! Vendor {v_id}: Year/Week must be int he format YYYYWW.")
    is_valid = False 
  else:
    week_num = int(year_week[4:])
    if week_num < 1 or week_num > 52:
      print(f"ERROR! Vendor {v_id}: Week must be between 1-52.")
      is_valid = False 

# Validaiton 4
  if int(i["Veg_dogs_sold"]) % 10 != 0:
    print(f"ERROR! Vendor {v_id}: Veggie sales must end in a 0.")
    is_valid = False 
# Validation 5
  if int(i["Meat_dogs_sold"]) % 10 != 0:
    print(f"ERROR! Vendor {v_id}: Meat sales must end in a 0.")
    is_valid = False 

# Validation 6
  onions = float(i["Onions"])
  if (onions * 2) % 1 != 0:
    print(f"ERROR! Vendor {v_id}: Onions must be in 0.5Kg increments")
    is_valid = False 
# Validation 7 
  ketchup = int(i["Ketchup_L"])
  if ketchup < 1 or ketchup > 4:
    print(f"ERROR! Vendor {v_id}: ketchup must be between 1-4 Litres.")
    is_valid = False 

  if is_valid:
    final_data.append(i)
# ----- SECTION 3 RESULTS ----- # 
print(f"\nProcessing complete. {len(final_data)} valid records kept.")
for valid_item in final_data:
  print(f"Kept: {valid_item['V_ID']} - {valid_item['Year_and_week']}")
