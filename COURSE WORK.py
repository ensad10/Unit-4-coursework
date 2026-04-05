# Vendor ID 
# Vendor name (Done)
# Year and Week 
# Number of vegan hotdogs (Done)
# Number of meat hotdogs (Done)
# Onions (Kg) (Done)
# Ketchup (Litres) (Done)

# validation checking - so the code doesnt crash if file name is changed 
# find the file (Hotdogs.txt) and make a chest to put our end results (final_data).
def load_logs(file_needed = "hotdogs.txt"):
  final_data = []
  try:
    hotdog_file = open(file_needed, "r")  
# temporary give hotdogs.txt the nickname hotdogs_file
# because we are trying this line of code python wont just crash.
    for line in hotdog_file:
      columns = line.strip().split(",")
# this splits up the data everytime there is a comma becoming seperate lines.

      if len(columns) == 7:
# Validation 1: Vendor ID 
      /too do next:
# validation 2: Name length, This checks if the Vendors name is actually valid.      
        if len(colums[1]) < 2 or len(colums[1]) > 25:
          print(f"Invalid! Your name is too short or long."!)
# Validation 3: Year and week 
      /too do next:
# validation 4/5: Hotdog sales, This checks if both veg and meat hotdogs sold are divisable by 10.
        if int(columns[3]) % 10 != 0:
          print(f"Invalid! Hotdog sales have to end in a 0.")
          continue 
        if int(columns[4]) % 10 != 0:
          print(f"Invalid! Hotdog sales have to end in a 0.")
          continue
# Validation 6: Onion 
        if float(columns[5]) <= 0
# validation 7: Ketchup, This checks if Ketchup must be between 1 and 4 Litres.
        if int(columns[6]) <1 or int(columns[6]) > 4:
          print(f"Invalid! Ketchup must be between 1 and 4 litres.")
          continue 
        
        record = {
          "V_ID": columns[0],
          "V_Name": columns[1].lower()
          "Year_and_week": columns[2],
          "Veg_dogs_sold": int(columns[3]),
          "Meat_dogs_sold": int(columns[4]),
          "Onions": float(columns[5]),
          "Ketchup_L": int(columns[6]),
        }
        final_data.append(record)
# (record) is basically the workers profiles. 
# which is stored in the (final_data) a storage container.
  hotdog_file.close()
  print(f"Successfully loaded {len(final_data)} records.")
  return final_data
# all this does is close the the actual hotdog.txt file and prints a message with organised profiles.


# linear search - this checks the items one by one in order until the item is matched.
def linear_check (data, target_name):
  for vendor in data:
    if vendor["name"] == target_name:
      return vendor
  return None 

# Binary search - checks the data by halving the (data set) until the item is matched 
# The data set MUST be sorted first
def binary_search (data, target_name):
  
