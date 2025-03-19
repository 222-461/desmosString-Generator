# Automated Coordinate-Based Art - Step 0

# Libraries

import aCBA_S1
import aCBA_S2
import aCBA_S3

import time

# Constants

PROCESS = [aCBA_S1, aCBA_S2, aCBA_S3]

# Variables

index = 0

# Main Program

for index in range(len(PROCESS)):
    PROCESS[index]()
    print(f"Step {index + 1} Successfully Executed.")
    time.sleep(1)
    

