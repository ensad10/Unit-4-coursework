import time

# Helper list to keep track of what each index means
# 0:ID, 1:Name, 2:Week, 3:Veg, 4:Meat, 5:Onions, 6:Ketchup
header_list = ["ID", "Name", "Week", "Veg", "Meat", "Onions", "Ketchup"]
def load_data(filename):
    final_data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                items = line.strip().split(',')
# Standard check to ensure row is complete
                if len(items) == 7:
                    final_data.append(items)
    except:
        print("Could not find or read the file!")
        
    return final_data

records = load_data('external.file.txt')

def validation_check(records):
    clean_data = []
    for row in records:
# Check Vendor ID (Uppercase, 2 letters, underscore, 3 digits)
        if len(row[0]) != 6 or not row[0][:2].isupper() or not row[0][:2].isalpha() or row[0][2] != '_' or not row[0][3:].isdigit():
            continue

# Check Vendor name (between 2 and 25 characters)
        if len(row[1]) < 2 or len(row[1]) > 25:
            continue

# Check Year and Week (YYYYWW format, week between 1 and 52)
        if len(row[2]) != 6 or not row[2].isdigit():
            continue
        week_part = int(row[2][4:])
        if week_part < 1 or week_part > 52:
            continue

# Check if the veg dogs sold are divisible by 10
        if int(row[3]) % 10 != 0:
            continue

# Check if the meat dogs sold are divisible by 10
        if int(row[4]) % 10 != 0:
            continue

# Check if the onions are in Increments of 0.5
        if float(row[5]) % 0.5 != 0:
            continue

# Check if the ketchup is an integer between 1 and 4
        if int(row[6]) < 1 or int(row[6]) > 4:
            continue

# If it passed all 'continue' checks, add to clean_data
        clean_data.append(row)

    print("~ After the validation check only", len(clean_data), "out of", len(records), "records have passed successfully ~")
    return clean_data

records = load_data('Hotdogs.txt') 
main_data = validation_check(records)

# --- SEARCHING SECTION ---

def linear_search_unsorted(data, target, col):
    results_found = []
    search_term = target.lower()
    
    for item in data:
        current_value = item[col].lower()
        # Check every single row to find every match
        if current_value == search_term:
            results_found.append(item)
            
    return results_found

def linear_search_sorted(data, target, col):
    results_found = []
    search_term = target.lower()
    
    for item in data:
        current_value = item[col].lower()
        
        if current_value == search_term:
            results_found.append(item)
        elif current_value > search_term:
# Stop searching because the data is sorted alphabetically/numerically
# and we have passed where the target would be
            break
            
    return results_found

def binary_search(data, target, col):
    low_index = 0
    high_index = len(data) - 1
    found_list = []
    search_term = target.lower()
    
    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        mid_val = data[mid_index][col].lower()
        
        if mid_val == search_term:
# We found a match, now we must look around it for duplicates
            found_list.append(data[mid_index])
            
# Check the items to the left (backwards)
            left_pointer = mid_index - 1
            while left_pointer >= 0:
                if data[left_pointer][col].lower() == search_term:
                    found_list.append(data[left_pointer])
                    left_pointer = left_pointer - 1
                else:
                    break
# No more matches this way therefore we stop the code 
            
# Check the items to the right (forwards)
            right_pointer = mid_index + 1
            while right_pointer < len(data):
                if data[right_pointer][col].lower() == search_term:
                    found_list.append(data[right_pointer])
                    right_pointer = right_pointer + 1
                else:
                    break
# No more matches this way therefore we stop the code 
            
            return found_list 
            
        elif mid_val < search_term:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1
            
    return found_list

# --- SORTING SECTION ---

def bubble_sort(data, col):
# Standard bubble sort using nested loops and a temp variable
    data_length = len(data)
    for i in range(data_length):
        for j in range(0, data_length - i - 1):
            
# Decide if we are comparing as numbers or text
            if col >= 3:
                val1 = float(data[j][col])
                val2 = float(data[j+1][col])
            else:
                val1 = data[j][col].lower()
                val2 = data[j+1][col].lower()
            
            if val1 > val2:
# Perform the actual swap
                temporary_storage = data[j]
                data[j] = data[j+1]
                data[j+1] = temporary_storage
                
    return data

def quick_sort(data, col):
# If the list is empty or has 1 item, it's already "sorted"
    if len(data) <= 1:
        return data
    
# Selecting the middle element as the pivot
    middle_index = len(data) // 2
    pivot_row = data[middle_index]
    
    if col >= 3:
        pivot_val = float(pivot_row[col])
    else:
        pivot_val = pivot_row[col].lower()
        
    left_side = []
    middle_side = []
    right_side = []
    
# Manually looping and sorting into the three temporary lists
    for row in data:
        if col >= 3:
            current_compare = float(row[col])
        else:
            current_compare = row[col].lower()
            
        if current_compare < pivot_val:
            left_side.append(row)
        elif current_compare == pivot_val:
            middle_side.append(row)
        else:
            right_side.append(row)
    
# Use recursion to sort the left and right, then join them
    sorted_result = quick_sort(left_side, col) + middle_side + quick_sort(right_side, col)
    return sorted_result

#~~~~~
# SAVING DATA
#~~~~~
def save_data_to_file(data_list, filename):
    # Open the file in 'w' mode (write mode)
    # This will overwrite the file or create a new one if it doesn't exist
    try:
        file_out = open(filename, 'w')
        
        for row in data_list:
            # We need to turn each list of data into a single string separated by commas
            # We use str() on each item just in case some are numbers
            line_to_save = str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + \
                           str(row[3]) + "," + str(row[4]) + "," + str(row[5]) + "," + \
                           str(row[6])
            
            # Write the string and add a newline character so the next row starts on a new line
            file_out.write(line_to_save + "\n")
            
        file_out.close()
        print("Success: Data has been saved to " + filename)
        
    except Exception as e:
        print("An error occurred while saving: " + str(e))

# MAIN APPLICATION LOOP 

def run_app():
    # Load and clean the data immediately when starting
    records = load_data('Hotdogs.txt')
    
    keep_running = True
    while keep_running == True:
        print("\n" + "="*30)
        print("   HOTDOG VENDOR SYSTEM")
        print("="*30)
        print("1. Unsorted Linear Search")
        print("2. Sorted Linear Search")
        print("3. Binary Search")
        print("4. High/Low Analysis")
        print("5. Performance Race")
        print("6. Bubble Sort")
        print("7. Quick Sort")
        print("8. Exit")
        
        user_choice = input("\nSelect an option: ")
        
        if user_choice == "8":
            print("\nExiting System... Have a nice day!")
            keep_running = False
            
        elif user_choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nAvailable Fields:")
            print("0:ID, 1:Name, 2:Week, 3:Veg, 4:Meat, 5:Onions, 6:Ketchup")
            
            try:
# Ask for the column using try and except for maximum robustness in my code 
                c_input = input("Enter column index (0-6): ") 
                c = int(c_input)
            except ValueError:
                print("Invalid input. Please enter a number for the column.")
                continue

            if user_choice == "1":
                t = input("Enter value to search for: ")
                results = linear_search_unsorted(main_data, t, c)
                print("\nSearch Results:")
                for r in results: 
                    print(r)

            elif user_choice == "2":
                t = input("Enter value to search for: ")
# Use the faster sort before searching so that it takes less time for the search to actually happen 
                sorted_list = quick_sort(main_data, c)
                results = linear_search_sorted(sorted_list, t, c)
                print("\nSearch Results:")
                for r in results: 
                    print(r)

            elif user_choice == "3":
                t = input("Enter value to search for: ")
                sorted_list = quick_sort(main_data, c)
                results = binary_search(sorted_list, t, c)
                print("\nSearch Results:")
                for r in results: 
                    print(r)

            elif user_choice == "4":
                # Sort first to find high and low easily
                sorted_list = quick_sort(main_data, c)
                lowest_record_val = sorted_list[0][c]
                highest_record_val = sorted_list[-1][c]
                
                analysis_results = []

                # --- PROCESS LOWEST ---
                print(f"\n--- RECORDS WITH LOWEST VALUE ({lowest_record_val}) ---")
                analysis_results.append(f"--- RECORDS WITH LOWEST VALUE ({lowest_record_val}) ---\n")
                for row in sorted_list:
                    if row[c] == lowest_record_val:
                        print(row)
                        # Formatting the row as a string for the file
                        analysis_results.append(", ".join(row) + "\n")
                    else:
                        break

                # --- PROCESS HIGHEST ---
                print(f"\n--- RECORDS WITH HIGHEST VALUE ({highest_record_val}) ---")
                analysis_results.append(f"\n--- RECORDS WITH HIGHEST VALUE ({highest_record_val}) ---\n")
                # Loop backwards from the end
                for i in range(len(sorted_list)-1, -1, -1):
                    if sorted_list[i][c] == highest_record_val:
                        print(sorted_list[i])
                        analysis_results.append(", ".join(sorted_list[i]) + "\n")
                    else:
                        break

                # --- SAVE SECTION ---
                save_confirm = input("\nWould you like to save these specific records to a file? (y/n): ")
                if save_confirm.lower() == 'y':
                    out_name = input("Enter filename for analysis (e.g., high_low_report.txt): ")
                    
                    try:
                        with open(out_name, "a") as f:
                            f.write("\n" + "="*40 + "\n")
                            f.write("~ HIGHEST AND LOWEST VALUE RESULTS ~\n")
                            f.write(f"Generated on column: {header_list[c]}\n")
                            f.write("="*40 + "\n")
                            # Write each line stored in analysis_results
                            f.writelines(analysis_results)
                        print(f"Successfully saved analysis to {out_name}")
                    except Exception as e:
                        print(f"An error occurred while saving: {e}")
                

            elif user_choice == "5":
                t = input("Target value for the race: ")
                
# Race 1: Unsorted Linear
                start_time_1 = time.time()
                linear_search_unsorted(main_data, t, c)
                end_time_1 = time.time()
                duration_1 = end_time_1 - start_time_1

# Race 2: Sorted Linear
                sorted_list = quick_sort(main_data, c)
                start_time_sl = time.time()
                linear_search_sorted(sorted_list, t, c)
                end_time_sl = time.time()
                duration_sl = end_time_sl - start_time_sl
                
# Race 3: Binary Search
                start_time_2 = time.time()
                binary_search(sorted_list, t, c)
                end_time_2 = time.time()
                duration_2 = end_time_2 - start_time_2

# Extra: Sort Comparison
                start_bubble = time.time()
                bubble_sort(list(main_data), c)
                end_bubble = time.time()
                duration_bubble = end_bubble - start_bubble

                start_quick = time.time()
                quick_sort(main_data, c)
                end_quick = time.time()
                duration_quick = end_quick - start_quick
                
# Format to 8 decimal places as requested for a cleaner looking timer which is what i want 
                print("\n#~~~~~\nUnsorted Linear search took: " + format(duration_1, '.8f') + " seconds\n#~~~~~")
                print("#~~~~~\nSorted Linear search took: " + format(duration_sl, '.8f') + " seconds\n#~~~~~")
                print("#~~~~~\nBinary search took: " + format(duration_2, '.8f') + " seconds\n#~~~~~")
                print("#~~~~~\nBubble Sort took: " + format(duration_bubble, '.8f') + " seconds\n#~~~~~")
                print("#~~~~~\nQuick Sort took: " + format(duration_quick, '.8f') + " seconds\n#~~~~~")

            elif user_choice == "6":
# This changes the main_data order permanently which is important 
                sorted_results = bubble_sort(main_data, c)
                print("\nData Sorted by Bubble Sort:")
                for r in sorted_results: 
                    print(r)

            elif user_choice == "7":
                sorted_results = quick_sort(main_data, c)
                print("\nData Sorted by Quick Sort:")
                for r in sorted_results: 
                    print(r)
        else:
            print("Invalid menu choice. Please try again.")
                
# Call the app to start (basically the main part of the program)
if __name__ == "__main__":
    run_app()
