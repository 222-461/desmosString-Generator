# ========================================================================================================================
# aCBA Generator REWRITE v0.1
# ========================================================================================================================

# Libraries

import math
import ast
import os

# Constants

INPUTGEN = "aCBA_generatorExport.txt"  # S2 INPUT

OUTPUTPOINTS = "aCBA_pointExport.txt"  # S1 OUTPUT & S3 INPUT
OUTPUTPINS = "aCBA_pinExport.txt"      # S2 OUTPUT & and S3 INPUT

OUTPUTCOORDINATES = "aCBA_coordinateExport.txt"  # S3 OUTPUT & S4 INPUT 
OUTPUTREFLECT = "aCBA_OUTPUT.txt"     # S4 INPUT & OUTPUT

WIPELIST = [OUTPUTCOORDINATES,
            OUTPUTREFLECT,
            OUTPUTPINS,
            OUTPUTPOINTS]

# Variable

setting = ""

# Subprograms

def aCBA_S1(pInputPin):
    
    # Local Variable Initialization
    
    coordinates = []

    # aCBA_S1 Main Process

    circleRadius = float(input("Radius: "))
    circlePins = int(input("Pins: "))
    deltaTheta = (2 * math.pi) / circlePins

    # Pin Coordinate Generation
    with open(pInputPin, "w") as exportPoints:
        for index in range(circlePins):
            theta = index * deltaTheta
            axisX = circleRadius * math.cos(theta)
            axisY = circleRadius * math.sin(theta)
            coordinates.append((axisX, axisY))

        for index, (axisX, axisY) in enumerate(coordinates):
            print(f"Point {index+1}: ({axisX:.10f}, {axisY:.10f})")
            exportPoints.write(f"[{index + 1}, {axisX}, {axisY}]\n")

    print("Stage 1 - Successful Execution")

def aCBA_S2(pInputGenerator, pOutputPin):
    
    # aCBA_S2 Main Process
    
    with open(pInputGenerator, "r") as stringData:
        rawData = stringData.read().strip()
        # Handle data split across lines
        if '\n' in rawData:
            rawData = rawData.replace('\n', ',')
        listData = [int(x.strip()) for x in rawData.split(',') if x.strip()]

    with open(pOutputPin, "w") as exportData:
        exportData.write(str(listData))

    print("Stage 2 - Successful Execution")

def aCBA_S3(pCirclePoints, pImportPin, pOutputCoord):
    
    # Subprograms
    
    def evalState(line):
        try:
            return ast.literal_eval(line.strip())
        except:
            return None

    # aCBA_S3 Main Process

    pointExportData = {}
    
    # Read and process circle points
    with open(pCirclePoints, "r") as pointExportFile:
        for line in pointExportFile:
            data = evalState(line)
            if data and len(data) == 3:
                pointExportData[data[0]] = (data[1], data[2])

    # Read and process pin positions
    with open(pImportPin, "r") as pinExportFile:
        pinData = evalState(pinExportFile.read())
        if not pinData:
            pinData = []

    # Generate coordinate pairs
    desmosLines = []
    for index in range(len(pinData) - 1):
        current = pinData[index]
        nextPin = pinData[index + 1]
        if current in pointExportData and nextPin in pointExportData:
            x1, y1 = pointExportData[current]
            x2, y2 = pointExportData[nextPin]
            desmosLines.append(f"({x1},{y1}),({x2},{y2})")

    # Write output
    with open(pOutputCoord, "w") as outputFile:
        for line in desmosLines:
            outputFile.write(line + "\n")

    print("Stage 3 - Successful Execution")

def aCBA_S4(pInputPath, pOutputPath):
    
    # Local Variable Initialization
    axisX = 0
    axisY = 0
    coordinateReflected = ""

    # Subprograms
    def axisXReflection(point):
        axisX, axisY = point
        return (axisX, -axisY)

    def axisYReflection(point):
        axisX, axisY = point
        return (-axisX, axisY)

    def importData(pImportPath):
        with open(pImportPath, "r") as coordinateList:
            lines = coordinateList.readlines()
        
        coordinates = []
        for line in lines:
            # Remove any whitespace and split into pairs
            pairs = line.strip().split("),(")
            for pair in pairs:
                # Remove any remaining parentheses and split into axisX and axisY
                axisX, axisY = pair.replace("(", "").replace(")", "").split(",")
                coordinates.append((float(axisX), float(axisY)))
        
        return coordinates

    def exportData(pOutputPath, coordinates):
        with open(pOutputPath, "w") as coordinateList:
            for index in range(0, len(coordinates), 2):
                # Write pairs of points as lines
                point1 = coordinates[index]
                point2 = coordinates[index + 1]
                coordinateList.write(f"({point1[0]},{point1[1]}),({point2[0]},{point2[1]})\n")

    # aCBA_S4 Main Process
    # Read the original coordinates
    coordinates = importData(OUTPUTCOORDINATES)

    # Get reflection axis
    reflectValidation = False
    while not reflectValidation:
        axis = input("Reflect over X-axis / Y-axis / Skip? (x/y/s): ").strip().lower()
        
        if axis == "x":
            coordinateReflected = [axisXReflection(point) for point in coordinates]
            reflectValidation = True
        elif axis == "y":
            coordinateReflected = [axisYReflection(point) for point in coordinates]
            reflectValidation = True
        elif axis == "s":
            coordinateReflected = coordinates.copy()
            reflectValidation = True
        else:
            print("Invalid input. Please enter x or y.")
        
    # Export reflected coordinates
    exportData(OUTPUTREFLECT, coordinateReflected)
        
    print("Stage 4 - Successful Execution")

def aCBA_S5(pGenFile, pWipe):
    
    # Local Variable Initialization

    index = 0

    # aCBA_S5 Main Process

    # Iteration through WIPELIST to wipe files
    while index < len(pWipe):
        try:
            os.remove(pWipe[index])
            print(pWipe[index], "successfully deleted")
        except:
            print(pWipe[index], "does not exist")
        index += 1

    # Wipes initial coordinate file
    with open(pGenFile, "w") as openFile:
        openFile.truncate(0)

    print("aCBA_generatorExport.txt successfully wiped")
    print("Stage 5 - Successful Execution")

# Main Program

aCBA_S1(OUTPUTPOINTS) # Generate Pin Positions
aCBA_S2(INPUTGEN, OUTPUTPINS) # Convert Format
aCBA_S3(OUTPUTPOINTS, OUTPUTPINS, OUTPUTCOORDINATES) # Generate Coordinates
aCBA_S4(OUTPUTCOORDINATES, OUTPUTREFLECT) # Reflection

# Wipe / Quit
while setting != "Q" and setting != "W":
    setting = str(input("Quit / Wipe (Q/W): "))
    setting = setting.upper()
    
    if setting == "W":
        aCBA_S5(INPUTGEN, WIPELIST) # Wipe Files

print("Program Successfully Terminated")
