# Automated Coordinate-Based Art - Step 3

# Constants

CIRCLEIMPORT = "aCBA_pointExport.txt"
PINIMPORT = "aCBA_pinExport.txt"
OUTPUTFILEPATH = "aCBA_coordinateExport.txt"

# Variables

exportData = ""
exportValues = []
pointExportData = {}
desmosLines = []

# Subprograms

def processExport(exportData):
    
    exportData = exportData.strip("[]")
    return [int(item.strip().strip("'")) for item in exportData.split(",")]

def processPoint(pointExportData):
 
    pointExportData = pointExportData.strip("[]")
    return [item.strip() for item in pointExportData.split(",")]

# Main Program

# Read the circle points file
with open(CIRCLEIMPORT, "r") as pointExportFile:
    pointExportLines = pointExportFile.readlines()

# Read the pin positions file
with open(PINIMPORT, "r") as pinExportFile:
    exportData = pinExportFile.readline().strip()

    # Process the export data to get indices
    exportValues = processExport(exportData)

# Process the point export data
for line in pointExportLines:
    cleanedLine = line.strip()
    parsedLine = processPoint(cleanedLine)
    
    # Extract index, x-coordinate, and y-coordinate
    index = int(parsedLine[0])
    axisX = float(parsedLine[1])
    axisY = float(parsedLine[2])
    pointExportData[index] = (axisX, axisY)

# Generate pairs of coordinates for drawing lines
for index in range(len(exportValues) - 1):
    currentIndex = exportValues[index]
    nextIndex = exportValues[index + 1]
    
    # Get the coordinates for the current and next indices
    if currentIndex in pointExportData and nextIndex in pointExportData:
        currentPoint = pointExportData[currentIndex]
        nextPoint = pointExportData[nextIndex]
        line = f"({currentPoint[0]},{currentPoint[1]}),({nextPoint[0]},{nextPoint[1]})"
        desmosLines.append(line)

# Write the Desmos lines to the output file
with open(OUTPUTFILEPATH, "w") as outputFile:
    for line in desmosLines:
        outputFile.write(line + "\n")

outputFile.close()
pointExportFile.close()
pinExportFile.close()

print("Successful Execution.")

