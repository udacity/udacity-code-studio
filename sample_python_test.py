import sys, time
time.sleep(1)
sys.path.append('/home/student_files/steps')

import inventory
from inventory import *

inventory_correct = {"tents":{"single": 4, "double": 5},
"backpacks": {"small": 5, "medium": 8, "large": 3},
"energybars": {"chocolate": 20, "espresso": 15, "oatmeal": 10},
"shirts": {"small": 12, "medium": 5, "large": 10}}

try:
    if (inventory == inventory_correct):
        print ("\n Great Job. You correctly assigned the inventory dictionary.")
        pass
except NameError:
    print ("\n inventory is undefined or missing.")
else:
    if (inventory != inventory_correct):
        print ("\n There was an error. Check that the inventory dictionary was assigned correctly.")
