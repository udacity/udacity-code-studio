import sys
sys.path.append('/home/student_files/steps')

import inventory
from inventory import *

stock_correct = {"backpacks": 10,  "energybars": 20, "sunglasses": 7}

try:
    if (stock == stock_correct):
        print ("\n Great job! You successfully made the stock dictionary.")
        pass
except NameError:
    print ("\n stock is undefined or missing.")
else:
    if (stock != stock_correct):
        print ("\n There was an error. Check to make sure the stock dictionary was created and assigned correctly.")
