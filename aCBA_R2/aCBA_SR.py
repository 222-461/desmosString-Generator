# Automated Coordinate-Based Art - Step RESET

# Libraries

import os

# Variables

wipeList = ["aCBA_coordinateExport.txt",
            "aCBA_coordinateReflect.txt",
            "aCBA_pinExport.txt",
            "aCBA_pointExport.txt"]

index = 0

# Main Program

# Deletes generated files

while index < len(wipeList):
    
    try:
        os.remove(wipeList[index])
        print(wipeList[index],"successfully deleted")
        
    except:
        print(wipeList[index],"does not exist")
        
    index += 1

# Wipes initial coordinate file

with open("aCBA_generatorExport.txt","w") as openFile:

    openFile.truncate(0)

openFile.close()

print("aCBA_generatorExport.txt successfully wiped")

