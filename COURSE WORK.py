# START TIMER 
import time

#------------------
# LOAD MY DATA - changed from a dictionary to a list for efficency - 
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
