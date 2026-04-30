import time

#------------------
# LOAD MY DATA 
#------------------
# this is where loading the file takes place. 
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
# VALIDATE DATA this is where the validation checks are held.
#~~~~~

def validate_data(records):
    valid_records = []
    # these lines of code check Vendor ID is uppercase, two letters, underscore, three digits e.g. AB_123
    for record in records:
        if len(record[0]) != 6 or not record[0][:2].isupper() or not record[0][:2].isalpha() or record[0][2] != '_' or not record[0][3:].isdigit():
            continue
        # these lines of code check Vendor name is between 2 and 25 characters
        if len(record[1]) < 2 or len(record[1]) > 25:
            continue
        # these lines of code check if the Year and Week is in format YYYYWW and week is between 1 and 52
        if len(record[2]) != 6 or not record[2].isdigit() or (int(record[2][3:]) >= 1 and int(record[2][3:]) <= 52): 
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
            valid_records.append(record)
     # Because everything else has passed the checks this record is ready to be added to valid_records list
    print("~ After the validation check only", len(valid_records), "out of", len(records), "records have passed sucessfully ~\n")
    return valid_records

valid_records = validate_data(records)


#~~~~~
# SEARCHING this is where the searching functions are held
#~~~~~

def linear_search(records, options, higher_lower):
    search_choice = get_search_value(records, options)
    matches = []

    for record in records:
        if search_choice.upper().strip() == record[options].upper().strip():
            matches.append(record)

    if matches:
        print("\nFound:", len(matches))
        for row in matches:
            print(row)
    else:
        print("Not found")


def binary_search_all(records, target, column):
    low = 0
    high = len(records) - 1
    results = []

    target = str(target).upper()

    while low <= high:
        mid = (low + high) // 2
        mid_value = str(records[mid][column]).upper()

        if mid_value == target:

            # found one match
            results.append(records[mid])

            # check left side
            left = mid - 1
            while left >= 0 and str(records[left][column]).upper() == target:
                results.append(records[left])
                left -= 1

            # check right side
            right = mid + 1
            while right < len(records) and str(records[right][column]).upper() == target:
                results.append(records[right])
                right += 1

            return results

        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return []

#~~~~~
# Get_search_value this is where the user gets to either enter a value they are looking for in the dadt storage or use the following value given in the list below to search for.
#~~~~~

def get_search_value(records, column):
    values = sorted(set([r[column] for r in records]))

    print("\nChoose a value or type your own:")
    print("0) Type manually")

    for i, v in enumerate(values[:5], 1):
        print(f"{i}) {v}")

    choice = input("\nEnter number or press Enter: ")

    if choice == "":
        return input("Enter value: ")

    if choice.isdigit():
        choice = int(choice)

        if choice == 0:
            return input("Enter value: ")

        if 1 <= choice <= len(values[:5]):
            return values[choice - 1]

    print("Invalid choice, using manual input.")
    return input("Enter value: ")

#~~~~~
# SORTING this is where the sorting functions are held.
#~~~~~

def bubble_sort(records, key):
    data = records[:]
    n = len(data)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]

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


#~~~~~
# PERFORMANCE TEST this allows the user to choose when they want to see the comparison of the bubble sort/quick sort or the linear searches and binary search. 
#~~~~~

def performance_test(valid_records):
    print("\n===== PERFORMANCE TEST =====")

    col = 1
    target = valid_records[0][col]  # automatic value (NO input)

    data_bubble = valid_records[:]
    data_quick = valid_records[:]

    # SORTING
    start = time.perf_counter()
    bubble_sort(data_bubble, col)
    bubble_time = time.perf_counter() - start

    start = time.perf_counter()
    sorted_quick = quick_sort(data_quick, col)
    quick_time = time.perf_counter() - start

    print("\n--- Sorting ---")
    print("Bubble Sort:", bubble_time)
    print("Quick Sort:", quick_time)

    # SEARCHING
    def linear_search_test(records, target, col):
        for record in records:
            if record[col] == target:
                return record

    start = time.perf_counter()
    linear_search_test(valid_records, target, col)
    lin_unsorted = time.perf_counter() - start

    start = time.perf_counter()
    linear_search_test(sorted_quick, target, col)
    lin_sorted = time.perf_counter() - start

    start = time.perf_counter()
    binary_search_all(sorted_quick, target, col)
    binary_time = time.perf_counter() - start

    print("\n--- Searching ---")
    print("Linear (unsorted):", lin_unsorted)
    print("Linear (sorted):  ", lin_sorted)
    print("Binary Search:    ", binary_time)

    print("===============\n")

#~~~~~
# HIGH LOW this is where the user can choose if they want the highest/lowest value or both to be outputted when picking their options. 
#~~~~~

def high_low(records, column, choice):

    highest = float('-inf')
    lowest = float('inf')

    high_matches = []
    low_matches = []

    # find highest and lowest first
    for i, record in enumerate(records, start=1):

        value = float(record[column]) if column == 5 else int(record[column])

        if value > highest:
            highest = value

        if value < lowest:
            lowest = value

    # collect ALL matches after we know values
    for i, record in enumerate(records, start=1):

        value = float(record[column]) if column == 5 else int(record[column])

        if value == highest:
            high_matches.append((i, record))

        if value == lowest:
            low_matches.append((i, record))

    # OUTPUT
    if choice == 1 or choice == 3:
        print("\nHIGHEST VALUE:", highest)
        for index, record in high_matches:
            print(f"Index {index} | {record}")

    if choice == 2 or choice == 3:
        print("\nLOWEST VALUE:", lowest)
        for index, record in low_matches:
            print(f"Index {index} | {record}")


#~~~~~
# SAVE RESULTS this is where the output of the options they pick will be saved onto a seperate .txt file. 
#~~~~~

def save_results_to_file(results, filename="results.txt"):
    try:
        with open(filename, "a") as file:

            if results:
                if isinstance(results[0], list):
                    for r in results:
                        file.write(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]}\n")
                else:
                    file.write(f"{results[0]} | {results[1]} | {results[2]} | {results[3]} | {results[4]} | {results[5]} | {results[6]}\n")
            else:
                file.write("No results found\n")

        print("\nResults saved to 'results.txt'")

    except:
        print("Error saving file")


#~~~~~
# MENU # this is where the user can chose what options they want to do and how the code works (they can control it) 
#~~~~~
def print_record(record):
    print(
        f"{record[0]} | {record[1]} | {record[2]} | "
        f"{record[3]} | {record[4]} | {record[5]} | {record[6]}"
    )
def search_question():
    search_choice = int(input(
        "\nWhat Would you like to do? (1-5)\n"
        "1) Linear search (unsorted)\n"
        "2) Linear search (sorted)\n"
        "3) Binary search\n"
        "4) Performance test\n"
        "5) High_Low\n"
        "6) Exit\n\n< "
    ))

    while search_choice >= 1 or search_choice <= 6:
        if search_choice == 1:
            options = int(input("\nChoose a column\n(0) Vendor ID \n(1) Vendor Name \n(2) YYYYWW \n(3) Veg Hotdogs Sold \n(4) Meat Hotdogs sold \n(5) Onions \n(6) Ketchup Used\n\n< "))
            linear_search(valid_records, options, 0)
            search_question()

        elif search_choice == 2:
            options = int(input("\nChoose a column\n(0) Vendor ID \n(1) Vendor Name \n(2) YYYYWW \n(3) Veg Hotdogs Sold \n(4) Meat Hotdogs sold \n(5) Onions \n(6) Ketchup Used\n\n< "))
            sorted_data = quick_sort(valid_records[:], options)
            linear_search(sorted_data, options, 0)
            search_question()

        elif search_choice == 3:

            col = int(input("\nChoose a column\n(0) Vendor ID \n(1) Vendor Name \n(2) YYYYWW \n(3) Veg Hotdogs Sold \n(4) Meat Hotdogs sold \n(5) Onions \n(6) Ketchup Used\n\n< "))

            sorted_data = quick_sort(valid_records[:], col)
            target = get_search_value(valid_records, col)
            result = binary_search_all(sorted_data, target, col)

            print("\nResult:\n")

            if result:
                if isinstance(result[0], list):
                    for record in result:
                        print(record)
                else:
                    print(result)
            else:
                print("No results found")
            save_results_to_file(result)

            if result:
                if isinstance(result[0], list):
                    for record in result:
                        print(f"{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]} | {record[5]} | {record[6]}")

                else:
                    print(f"{result[0]} | {result[1]} | {result[2]} | {result[3]} | {result[4]} | {result[5]} | {result[6]}")

            else:
                print("No results found")
            search_question()
    
        elif search_choice == 4:
            performance_test(valid_records)
            search_question()

        elif search_choice == 5:
            column = int(input("\nChoose a column\n\n(3) Veg Hotdogs Sold \n(4) Meat Hotdogs sold \n(5) Onions \n(6) Ketchup Used\n\n< "))
            choice = int(input("1) Highest  2) Lowest  3) Both\n"))

            high_low(valid_records, column, choice)
            search_question()
            
        elif search_choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid option")
            search_question()


# RUN
search_question()
