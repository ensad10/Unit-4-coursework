# START TIMER 
import time

#------------------
# LOAD MY DATA
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
records = load_data('Hotdogs.txt')
    
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


valid_records = validate_data(records)

def high_low(records, tracker, length_tracker, maximum, highOrlow):
    if highOrlow == 1:
        if len(tracker) and len(length_tracker) != 0:
            print("Highest: ", tracker, " index: ", length_tracker)

    elif highOrlow == 2:   
        if len(tracker) and len(length_tracker) != 0:
            print("Lowest: ", tracker, " index: ", length_tracker)

    else:
        print("Highest: ", maximum, " index: ", tracker_length)
        print("Lowest: ", maximum, " index: ", tracker_length)
    
def linear_search(records, options, higher_lower):
    highest = 0 # has too be zero so numbers can surpass it. 
    lowest = 100000000000000000000000000 # has too be low so nothing surpasses it.
    high_list = [] # Empty
    low_list = [] # Empty 
    index_list = [] # Empty
    name_date = []

    if options == 3 or options == 4 or options == 6:
        index = 1 # index has to start at 1 (basically the first line)
        if higher_lower == 1: # if the user input is 1 then the loop begins here
            for record in records:
                if int(record[options]) > highest: # if record (1-7 e.g Vendor ID, Vendor Name etc..) is bigger than highest continue through the loop.
                    highest = int(record[options]) 

            for i in records:
                if int(i[options]) == highest: # if i is the highest value find the index and put it into the index.list 
                    index_list.append(index) 
                    high_list.append(int(i[options])) # this puts the highest value into the high.list
                index += 1 # this adds 1 too the index counter so that it matches the row of the highest value within the record(option)
            high_low(records, high_list, index_list, highest, higher_lower)

        if higher_lower == 2: # if higher_lower = 2 then we are looking for the lowest number 
            for record in records: 
                if int(record[options]) < lowest: 
                    lowest = int(record[options]) # checks in each record (line of data includes Vendor ID, V_name etc...) based on what the user inputs 

            for i in records:
                if int(i[options]) == lowest:
                    index_list.append(index)
                    low_list.append(int(i[options]))
                index += 1
            high_low(records, low_list, index_list, lowest, higher_lower)


    if options == 5:
        index = 1
        if higher_lower == 1:
            for record in records:
                if float(record[options]) > highest:
                    highest = float(record[options])

            for i in records:
                if float(i[options]) == highest:
                    index_list.append(index)
                    high_list.append(float(i[options]))
                index += 1
            high_low(records, high_list, index_list, highest, higher_lower)


        if higher_lower == 2:
            for record in records:
                if float(record[options]) < lowest:
                    lowest = float(record[options])

            for i in records:
                if float(i[options]) == lowest:
                    index_list.append(index)
                    low_list.append(float(i[options]))
                index += 1
            high_low(records, low_list, index_list, lowest, higher_lower)


    if options == 0 or options == 1 or options == 2:
        search_choice = input("Enter what name or date you are looking for: ")
        for record in records:
            if search_choice.upper() == record[options].upper():
                    name_date.append(record[options])
            else:
                continue
                    
        if len(name_date) == 0:
            print("Name not found in records. ")


#~~~~~
# SORTING
#~~~~~


def bubble_sort(records, key):
    data = records
    n = len(data)
    count = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
                if data[j][key] > data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    count += 1
    return data


def quick_sort(records, column):
    
    if len(records) <= 1:
        return records
    
    
    pivot = records[0]
    left = []
    right = []
    
    
    for item in records[1:]:
        
        if item[column] <= pivot[column]:
            left.append(item)
        else:
            right.append(item)
            
    
    return quick_sort(left, column) + [pivot] + quick_sort(right, column)

def binary_search(records, target, column):
    low = 0
    high = len(records) - 1
    
    while low <= high:
        mid = (low + high) // 2
       
        mid_value = str(records[mid][column]).upper()
        search_target = str(target).upper()
        
        if mid_value == search_target:
            return records[mid]  
        elif mid_value < search_target:
            low = mid + 1
        else:
            high = mid - 1
    return None 



