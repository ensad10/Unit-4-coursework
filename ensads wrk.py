import time

#Helper list to keep track of what each index means
#0:ID, 1:Name, 2:Week, 3:Veg, 4:Meat, 5:Onions, 6:Ketchup

header_list = ["ID", "Name", "Week", "Veg", "Meat", "Onions", "Ketchup"]
# --- LOADING SECTION ---

def load_data(filename):
    final_data = [] #Create a list for the data to be inserted 
    try: 
        with open(filename, 'r') as file:
            for line in file:
                items = line.strip().split(',')# Standard check to ensure row is complete
                if len(items) == 7:
                    final_data.append(items) #Add the data to the file 
    except:
        print("Could not find or read the file!") #Catch any errors such as invalid filename
        
    return final_data
# --- VALIDATION SECTION ---

def validation_check(records):
    clean_data = []
    for row in records:
#Check Vendor ID (Uppercase 2 letters, underscore 3 digits)
        if len(row[0]) != 6 or not row[0][:2].isupper() or not row[0][:2].isalpha() or row[0][2] != '_' or not row[0][3:].isdigit():
            continue
#Check Vendor name (between 2 and 25 characters)
        if len(row[1]) < 2 or len(row[1]) > 25:
            continue
#Check Year and Week (YYYYWW format week between 1 and 52)
        if len(row[2]) != 6 or not row[2].isdigit():
            continue
        week_part = int(row[2][4:])
        if week_part < 1 or week_part > 52:
            continue
#Check if the veg dogs sold are divisible by 10
        if int(row[3]) % 10 != 0:
            continue
#Check if the meat dogs sold are divisible by 10
        if int(row[4]) % 10 != 0:
            continue
#Check if the onions are in Increments of 0.5
        if float(row[5]) % 0.5 != 0:
            continue
#Check if the ketchup is an integer between 1 and 4
        if int(row[6]) < 1 or int(row[6]) > 4:
            continue
#If it passed all the continue checks are added to the clean_data
        clean_data.append(row)

    print("~ After the validation check only", len(clean_data), "out of", len(records), "records have passed successfully ~")
    return clean_data

# --- SEARCHING SECTION ---

def linear_search_unsorted(data, target, col):

    results_found = [] #make and empty list to store all the matches found 
    search_term = target.lower() #convert each search target into a lowercase to make the search more reliable 
    
    for item in data: #Iterate through every row in the provided dataset
        current_value = item[col].lower() #Get the value from the specific column
        if current_value == search_term: #Check if the current value matches what we are looking for
            results_found.append(item)#if it matches add the entire row to our results list
            
    return results_found #Return the full list of matches (which will be empty if nothing was found)

def linear_search_sorted(data, target, col):
    results_found = [] 
    search_term = target.lower() 
    
    for item in data:
        current_value = item[col].lower()
        if current_value == search_term:
            results_found.append(item)
        elif current_value > search_term: #Since the list is sorted it is more optimized if the current value is
#greater than the target, the target cannot exist any further down the list 
            break #Exit the loop early to save time and processing power
        
    return results_found #Return the matches found before the break occurred

def binary_search(data, target, col):
#set the boundaries i need in the function for the search
    low_index = 0
    high_index = len(data) - 1
    found_list = []
    
    search_term = target.lower()#Lowercase the target to keep the search case insensitive
    
    while low_index <= high_index: #Continue searching as long as the search window has at least one item
        mid_index = (low_index + high_index) // 2 #Calculate the middle point of the current search window
        mid_val = data[mid_index][col].lower()#Get the value at the middle index for the specified column

        if mid_val == search_term: #Finding a match for the middle position
            found_list.append(data[mid_index])#So we add the record we found to our results list
            #Check for any duplicates to the left
            left_pointer = mid_index - 1 
            while left_pointer >= 0:
                
                if data[left_pointer][col].lower() == search_term: #If the item to the left matches then add it and keep moving left
                    found_list.append(data[left_pointer])
                    left_pointer = left_pointer - 1
                else:
                    break #Stop if we hit a value that dont match
            
            #Check the items to the right
            right_pointer = mid_index + 1
            while right_pointer < len(data):
                if data[right_pointer][col].lower() == search_term: #If the item to the right matches then add it and keep moving right
                    found_list.append(data[right_pointer])
                    right_pointer = right_pointer + 1
                else:
                    break #Stop if we hit a value that dont match
            return found_list #Return all matches found immediately
            
        elif mid_val < search_term: #Check if the middle value is smaller than our target
            low_index = mid_index + 1
        else: #Check if the middle value is larger than our target
            high_index = mid_index - 1 
    return found_list

# --- SORTING SECTION ---

def bubble_sort(data, col):
    
    data_length = len(data) #Get the total number of records in the list
    for i in range(data_length): #This controls how many passes occur with this function
        for j in range(0, data_length - i - 1): #This prevents the code from re-checking sorted items at the end 
            

            if col >= 3: #Decide what were comparing (numbers or text) columns 3-6
                val1 = float(data[j][col]) #Conversion occurs here from str too floats 
                val2 = float(data[j+1][col])
            else:
                val1 = data[j][col].lower()#columns 0-2 and forces lowercases 
                val2 = data[j+1][col].lower()
            
            if val1 > val2: #This checks if the current items larger than the next 
                temporary_storage = data[j] #This performs the shift between the values 
                data[j] = data[j+1]
                data[j+1] = temporary_storage
                
    return data #Return the fully sorted list

def quick_sort(data, col):

    if len(data) <= 1: #This alone checks if the list is empty or only 1 value 
        return data #Meaning its already sorted so it returns it this stops recursion 
    

    middle_index = len(data) // 2 #This selects the middle value as the pivot 
    pivot_row = data[middle_index] #Using // to divde the list to get the middle value 
    
    if col >= 3: #This handles both text and numerals 
        pivot_val = float(pivot_row[col]) #Conversion to float for columns 3-6
    else:
        pivot_val = pivot_row[col].lower() #Conversion to lowercase for columns 0-2
        
    left_side = [] #Items smaller than the pivot 
    middle_side = [] #Items equal to the pivot 
    right_side = [] #Items larger than the pivot 
    
    for row in data: #This loops and sorts the rows into the 3 temporary lists 
        if col >= 3: 
            current_compare = float(row[col])
        else:
            current_compare = row[col].lower()
            
        if current_compare < pivot_val: #Checks the current row against the pivot and sorts it to the correct temporary list  
            left_side.append(row)
        elif current_compare == pivot_val:
            middle_side.append(row)
        else:
            right_side.append(row)
    

    sorted_result = quick_sort(left_side, col) + middle_side + quick_sort(right_side, col)
    return sorted_result #Rejoin the data in order once the splitting is complete 

# --- SAVING DATA SECTION ---

def ask_to_save(results_to_save, column_index, header_list, search_term=None):
    
    if not results_to_save: #Check to see if there is any data too save 
        print("\nNo results to save.")
        return

    confirm = input("\nWould you like to save these results to a file? (y/n): ") #Ask the user if they want to save the data 
    if confirm.lower() == 'y':
        filename = input("Enter filename (e.g., results.txt): ") #Get the filename they want to create/use 
        field_name = header_list[column_index]
        
        try:
            with open(filename, "a") as f: #Open the file in append mode so the data wont be reset/deleted
                f.write("\n" + "-"*30 + "\n") #Make a seperation line for a clearer display 
                f.write(f"FIELD: {field_name}\n")
                 
                if search_term: #If the user entered a search_term implement it into the file 
                    f.write(f"LOOKING FOR: {search_term}\n")
             
                f.write("-"*30 + "\n") #Close the header
                for item in results_to_save: #This loops through each item so that it is displayed 
                    if isinstance(item, list): #Conversion from list to string 
                        f.write(str(item) + "\n")
                    else: #Doesnt need conversion as its already a string 
                        f.write(str(item) + "\n")
            print(f"Successfully saved to {filename}") #Let the user know it was successful
        except Exception as e: #Catch any errors like invalid filenames
            print(f"Error saving to file: {e}")

# --- MAIN APPLICATION SECTION ---

def run_app():
    records = load_data('Hotdogs.txt') #Load and clean the data 
    main_data = validation_check(records) #Hotdogs.txt is fully loaded 
    
    keep_running = True #Keep the menu loop running 
    while keep_running == True: #While it is true keep looping 
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
        print("8. Exit") #Display the entire menu for the user 
        
        user_choice = input("\nSelect an option: ") #Get the users selection for the menu 
        
        if user_choice == "8": #Kill the code - if the user chooses this end the entire code
            print("\nExiting System... Have a nice day!")
            keep_running = False
            
        elif user_choice in ["1", "2", "3", "4", "5", "6", "7"]: #Validation check for the menu
            print("\nAvailable Fields:") #Shows the available fields the user can choose from
            print("0:ID, 1:Name, 2:Week, 3:Veg, 4:Meat, 5:Onions, 6:Ketchup")            
            try: #This prevents the app from crashing if a letter is inputted 
                c_input = input("Enter column index (0-6): ") 
                c = int(c_input)
            except ValueError:
                print("Invalid input. Please enter a number for the column.") #Restart the loop 
                continue
#-- CHOICE 1 --
            if user_choice == "1":
                t = input("Enter value to search for: ") #Get the target value 't' from the user 
                results = linear_search_unsorted(main_data, t, c) #Call the linear search function
                print("\nSearch Results:")
                
                for r in results: #Loop through the list print each row on a new line 
                    print(r)
                ask_to_save(results, c, header_list) #Offer too save the results 
#-- CHOICE 2 --    
            elif user_choice == "2":
                t = input("Enter value to search for: ") #Get the target value 't' from the user 
                sorted_list = quick_sort(main_data, c) #so we used quick sort to organize the data it too work correctly 
                results = linear_search_sorted(sorted_list, t, c) #We ran the linear search on a sorted list this time 
                print("\nSearch Results:")
                
                for r in results: #Loop through the list print each row on a new line
                    print(r)
                ask_to_save(results, c, header_list) #Offer too save the results 
#-- CHOICE 3 --
            elif user_choice == "3":
                t = input("Enter value to search for: ") #Get the target value 't' from the user 
                sorted_list = quick_sort(main_data, c) #Again we used quick sort to organize our data 
                results = binary_search(sorted_list, t, c) #I then ran the binary search function which only works on sorted lists 
                print("\nSearch Results:")

                for r in results: #Loop through the list print each row on a new line
                    print(r)
                ask_to_save(results, c, header_list) #Offer too save the results 


#-- CHOICE 4 --
            elif user_choice == "4":
                sorted_list = quick_sort(main_data, c) # Sort by the chosen column [c] to find high and low 
                lowest_val = sorted_list[0][c] 
                highest_val = sorted_list[-1][c] #Get all the HIGHEST and LOWEST values in the given column 
                
                analysis_results = [] #Make a list for all the data we want too keep (headers/records)

                # --- PROCESS LOWEST --- 
                header_low = f"--- RECORDS WITH LOWEST VALUE ({lowest_val}) ---" #Header of the lowest value that is being looked for 
                print("\n" + header_low)
                analysis_results.append(header_low)
                
                for row in sorted_list: #Iterate through the sorted list from start to end 
                    if row[c] == lowest_val: #Check if the current row matches (lowest value)
                        print(row)
                        analysis_results.append(row) #Add it to the results so that it can be saved 
                    else:
                        break #Once finished end the code here 

                # --- PROCESS HIGHEST ---
                header_high = f"--- RECORDS WITH HIGHEST VALUE ({highest_val}) ---" #Header of the highest value that is being looked for 
                print("\n" + header_high)
                analysis_results.append(header_high)
                
                for i in range(len(sorted_list)-1, -1, -1): #Iterate through the sorted list backwards from end to beginning 
                    if sorted_list[i][c] == highest_val:
                        print(sorted_list[i])
                        analysis_results.append(sorted_list[i]) #Add it to the results so that it can be saved 
                    else:
                        break #Once finished end the code here 
                
                ask_to_save(analysis_results, c, header_list) #Call the universal save function
                
            elif user_choice == "5":
                t = input("Target value for the race: ")
                
#1. Unsorted Linear
                start_time_1 = time.time() #Record the starting time of the search 
                res_1 = linear_search_unsorted(main_data, t, c) #Run the search based on the column given by the user 
                duration_1 = time.time() - start_time_1 #Calculate the speed 
                msg_1 = "" if res_1 else " (Value not found)"
#2. Sorted Linear
                sorted_list = quick_sort(main_data, c)
                start_time_sl = time.time() #Record the starting time of the search 
                res_sl = linear_search_sorted(sorted_list, t, c) #Run the search based on the column given by the user 
                duration_sl = time.time() - start_time_sl #Calculate the speed 
                msg_sl = "" if res_sl else " (Value not found)" 
#3. Binary Search
                start_time_2 = time.time() #Record the starting time of the search 
                res_2 = binary_search(sorted_list, t, c) #Run the search based on the column given by the user 
                duration_2 = time.time() - start_time_2 #Calculate the speed 
                msg_2 = "" if res_2 else " (Value not found)"
#4/5. Sorting Comparisons
                start_bubble = time.time() #Record the starting time of the sort
                bubble_sort(list(main_data), c) #Run the sort based on the column given by the user 
                duration_bubble = time.time() - start_bubble #Calculate the speed 

                start_quick = time.time() #Record the starting time of the sort
                quick_sort(main_data, c) #Run the sort based on the column given by the user 
                duration_quick = time.time() - start_quick #Calculate the speed 

#Prepare results for display and saving
                performance_results = [
                    f"Unsorted Linear search took: {format(duration_1, '.8f')} seconds{msg_1}",
                    f"Sorted Linear search took: {format(duration_sl, '.8f')} seconds{msg_sl}",
                    f"Binary search took: {format(duration_2, '.8f')} seconds{msg_2}",
                    f"Bubble Sort took: {format(duration_bubble, '.8f')} seconds",
                    f"Quick Sort took: {format(duration_quick, '.8f')} seconds"
                ]

                print("\n#~~ PERFORMANCE RACE RESULTS ~~#")
                for line in performance_results: #Print all the (performance) rows of results on a new line 
                    print(line)
                

                ask_to_save(performance_results, c, header_list, t) #Ask to save the results (save them with the target 't' in the header)
                
# CHOICE 6 
            elif user_choice == "6":
                sorted_results = bubble_sort(main_data, c) #Bubble sort through the list based on the column and field given by the user 
                print("\nData Sorted by Bubble Sort:") #Print the results of the data being Bubble sorted 
                for r in sorted_results: 
                    print(r)
                ask_to_save(sorted_results, c, header_list) #Offer too save the results 
                
            elif user_choice == "7":
                sorted_results = quick_sort(main_data, c) #Quick sort through the list based on the column and field given by the user 
                print("\nData Sorted by Quick Sort:") #Print the results of the data being quick sorted 
                for r in sorted_results: 
                    print(r)
                ask_to_save(sorted_results, c, header_list) #Offer too save the results 
        else:
            print("Invalid menu choice. Please try again.") #This checks for any errors and allows the user to try again 
                
# --- CALL THE APP SECTION ---
if __name__ == "__main__": 
    run_app()
