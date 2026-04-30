import time  # used for performance timing

#------------------
# LOAD MY DATA
#------------------

def load_data(filename):
    final_data = []  # stores all records from file
    
    try:
        with open(filename, 'r') as file:  # open file safely
            for line in file:
                # remove whitespace and split by comma
                items = line.strip().split(',')
                final_data.append(items)
                    
    except:
        # handles missing or unreadable file
        print("Could not find or read the file!")

    return final_data  # return all records

# load file into memory
records = load_data('Hotdogs.txt')


#~~~~~
# VALIDATE DATA
#~~~~~

def validate_data(records):
    valid_records = []  # stores only valid rows
    
    for record in records:

        # validate Vendor ID format (e.g. AB_123)
        if len(record[0]) != 6 or not record[0][:2].isupper() or not record[0][:2].isalpha() or record[0][2] != '_' or not record[0][3:].isdigit():
            continue
        
        # validate vendor name length
        if len(record[1]) < 2 or len(record[1]) > 25:
            continue

        # validate date format YYYYWW and week range
        if len(record[2]) != 6 or not record[2].isdigit() or (int(record[2][3:]) >= 1 and int(record[2][3:]) <= 52): 
            continue
        
        # veg hotdogs must be divisible by 10
        if int(record[3]) % 10 != 0:
            continue

        # meat hotdogs must be divisible by 10
        if int(record[4]) % 10 != 0:
            continue

        # onions must be in 0.5 increments
        if (float(record[5]) * 2).is_integer() == False:
            continue
        
        # ketchup must be between 1 and 4
        if int(record[6]) >= 1 and int(record[6]) <= 4:
            valid_records.append(record)

    print("~ After validation:", len(valid_records), "valid out of", len(records), "~\n")
    return valid_records

# store cleaned data
valid_records = validate_data(records)


#~~~~~
# SEARCHING
#~~~~~

def linear_search(records, options, higher_lower):
    # get value from user (or suggestions)
    search_choice = get_search_value(records, options)
    matches = []

    # loop through all records
    for record in records:
        # case-insensitive comparison
        if search_choice.upper().strip() == record[options].upper().strip():
            matches.append(record)

    # output results
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

    # standard binary search loop
    while low <= high:
        mid = (low + high) // 2
        mid_value = str(records[mid][column]).upper()

        if mid_value == target:

            results.append(records[mid])  # store match

            # scan LEFT for duplicates
            left = mid - 1
            while left >= 0 and str(records[left][column]).upper() == target:
                results.append(records[left])
                left -= 1

            # scan RIGHT for duplicates
            right = mid + 1
            while right < len(records) and str(records[right][column]).upper() == target:
                results.append(records[right])
                right += 1

            return results  # return all matches

        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return []  # no results found


#~~~~~
# GET SEARCH VALUE
#~~~~~

def get_search_value(records, column):
    # get unique values from column
    values = sorted(set([r[column] for r in records]))

    print("\nChoose a value or type your own:")
    print("0) Type manually")

    # show first 5 suggestions
    for i, v in enumerate(values[:5], 1):
        print(f"{i}) {v}")

    choice = input("\nEnter number or press Enter: ")

    # manual entry
    if choice == "":
        return input("Enter value: ")

    if choice.isdigit():
        choice = int(choice)

        if choice == 0:
            return input("Enter value: ")

        # return selected suggestion
        if 1 <= choice <= len(values[:5]):
            return values[choice - 1]

    print("Invalid choice, using manual input.")
    return input("Enter value: ")


#~~~~~
# SORTING
#~~~~~

def bubble_sort(records, key):
    data = records[:]  # copy to avoid modifying original
    n = len(data)
    
    # nested loops for comparison
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                # swap values
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def quick_sort(records, column):
    # base case
    if len(records) <= 1:
        return records
    
    pivot = records[0]  # choose first element
    left = []
    right = []
    
    # partition data
    for item in records[1:]:
        if item[column] <= pivot[column]:
            left.append(item)
        else:
            right.append(item)
            
    # recursive sort
    return quick_sort(left, column) + [pivot] + quick_sort(right, column)


#~~~~~
# PERFORMANCE TEST
#~~~~~

def performance_test(valid_records):
    print("\n===== PERFORMANCE TEST =====")

    col = 1
    target = valid_records[0][col]  # automatic test value

    data_bubble = valid_records[:]
    data_quick = valid_records[:]

    # measure bubble sort time
    start = time.perf_counter()
    bubble_sort(data_bubble, col)
    bubble_time = time.perf_counter() - start

    # measure quick sort time
    start = time.perf_counter()
    sorted_quick = quick_sort(data_quick, col)
    quick_time = time.perf_counter() - start

    print("\n--- Sorting ---")
    print("Bubble Sort:", bubble_time)
    print("Quick Sort:", quick_time)

    # simple linear search test
    def linear_search_test(records, target, col):
        for record in records:
            if record[col] == target:
                return record

    # timing comparisons
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
# HIGH / LOW ANALYSIS
#~~~~~

def high_low(records, column, choice):

    highest = float('-inf')
    lowest = float('inf')

    high_matches = []
    low_matches = []

    # find highest/lowest values
    for i, record in enumerate(records, start=1):
        value = float(record[column]) if column == 5 else int(record[column])

        if value > highest:
            highest = value

        if value < lowest:
            lowest = value

    # collect all matching records
    for i, record in enumerate(records, start=1):
        value = float(record[column]) if column == 5 else int(record[column])

        if value == highest:
            high_matches.append((i, record))

        if value == lowest:
            low_matches.append((i, record))

    # display results
    if choice == 1 or choice == 3:
        print("\nHIGHEST VALUE:", highest)
        for index, record in high_matches:
            print(f"Index {index} | {record}")

    if choice == 2 or choice == 3:
        print("\nLOWEST VALUE:", lowest)
        for index, record in low_matches:
            print(f"Index {index} | {record}")


#~~~~~
# SAVE RESULTS
#~~~~~

def save_results_to_file(results, filename="results.txt"):
    try:
        with open(filename, "a") as file:  # append mode

            if results:
                if isinstance(results[0], list):
                    for r in results:
                        file.write(" | ".join(r) + "\n")
                else:
                    file.write(" | ".join(results) + "\n")
            else:
                file.write("No results found\n")

        print("\nResults saved to 'results.txt'")

    except:
        print("Error saving file")


#~~~~~
# MENU SYSTEM
#~~~~~

def search_question():
    search_choice = int(input(
        "\nWhat Would you like to do?\n"
        "1) Linear search (unsorted)\n"
        "2) Linear search (sorted)\n"
        "3) Binary search\n"
        "4) Performance test\n"
        "5) High_Low\n"
        "6) Exit\n\n< "
    ))

    while search_choice >= 1 or search_choice <= 6:
        if search_choice == 1:
            options = int(input("Choose column (0-6): "))
            linear_search(valid_records, options, 0)
            search_question()

        elif search_choice == 2:
            options = int(input("Choose column (0-6): "))
            sorted_data = quick_sort(valid_records[:], options)
            linear_search(sorted_data, options, 0)
            search_question()

        elif search_choice == 3:
            col = int(input("Choose column (0-6): "))
            sorted_data = quick_sort(valid_records[:], col)
            target = get_search_value(valid_records, col)
            result = binary_search_all(sorted_data, target, col)

            print("\nResult:\n")

            if result:
                for record in result:
                    print(" | ".join(record))
            else:
                print("No results found")

            save_results_to_file(result)
            search_question()

        elif search_choice == 4:
            performance_test(valid_records)
            search_question()

        elif search_choice == 5:
            column = int(input("Choose column (3-6): "))
            choice = int(input("1) Highest  2) Lowest  3) Both\n"))
            high_low(valid_records, column, choice)
            search_question()
            
        elif search_choice == 6:
            print("Exiting program...")
            break

# RUN PROGRAM
search_question()
