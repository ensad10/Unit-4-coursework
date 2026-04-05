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

# validation checking - so the code doesnt crash if file name is changed 
# find the file (Hotdogs.txt) and make a chest to put our end results (final_data).
final_data = []
with open('Hotdogs.txt', 'r') as file:
  for line in file:
# this splits up the data everytime there is a comma becoming seperate items.
    items = line.strip().split(',')

    final_data.append(items)
# Validation starts here.
for i in (final_data):
  
# Validation 1: 
      /too do next:
  
# Validation 2: DONE!
  if len(i[1]) < 2 or len(i[1]) > 25:
    print(f"Invalid! Your name is too short.")

# Validation 3: Year and week 
      /too do next:

# validation 4/5: Hotdog sales, This checks if both veg and meat hotdogs sold are divisable by 10.
        if int(i[3]) % 10 != 0:
          print(f"Invalid! Hotdog sales have to end in a 0.")
          
        if int(i[4]) % 10 != 0:
          print(f"Invalid! Hotdog sales have to end in a 0.")
         
          
# Validation 6: Onion 
        if float(i[5]) <= 0

# validation 7: Ketchup, This checks if Ketchup must be between 1 and 4 Litres.
        if int(i[6]) <1 or int(i[6]) > 4:
          print(f"Invalid! Ketchup must be between 1 and 4 litres.")
         
        
        record = {
          "V_ID":(i[0]),
          "V_Name":(i[1]) ,
          "Year_and_week":(i[2]) ,
          "Veg_dogs_sold":(i[3]),
          "Meat_dogs_sold":(i[4]),
          "Onions":(i[5]),
          "Ketchup_L":(i[6]) ,
        }
        final_data.append(record)
# (record) is basically the workers profiles. 
# which is stored in the (final_data) a storage container.
        final_data.append(record)
                         
  print(f"Successfully loaded {len(final_data)} records.")
  return final_data
# This closes the the actual hotdog.txt file and prints a message with organised profiles.
# TIMER 
end = time.time()
length = end - start
print("it took ", length, " seconds") 

# linear search - this checks the items one by one in order until the item is matched.
def linear_check (data, target_name):
  for vendor in data:
    if vendor["name"] == target_name:
      return vendor
  return None 

# Binary search - checks the data by halving the (data set) until the item is matched 
# The data set MUST be sorted first
def binary_search (data, target_name):
  
