# Automated Coordinate-Based Art - Step 2

# Constants

GENINPUT = "aCBA_generatorExport.txt"
OUTPUTFILE = "aCBA_pinExport.txt"

# Variables

rawData = 0
stringData = 0

listData = []

# Main Program

# Convert raw data to list format
with open(GENINPUT,"r") as stringData:
    rawData = stringData.read()
    rawData = rawData.split(",")
    
    listData.append(rawData) 

# Export to file. 
with open(OUTPUTFILE, "w") as exportData:
    exportData.write(str(listData))
    
stringData.close()

print("Successful Execution")
