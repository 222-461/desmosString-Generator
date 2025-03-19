# Automated Coordinate-Based Art - Step 1

# Constants

OUTPUTFILE = "aCBA_pointExport.txt"

# Libraries

import math

# Variables

coordinates = []

circleRadius = 0.0
circlePins = 0.0

axisX = 0.0
axisY = 0.0

# Main Program

# Get circle dimensions
circleRadius = float(input("Radius: "))
circlePins = int(input("Pins: "))

# Calculation

deltaTheta = (2 * math.pi) / circlePins

with open(OUTPUTFILE,"w") as exportFile:

    # Calculation of coordinates
    for index in range(circlePins):
        theta = index * deltaTheta
        axisX = circleRadius * math.cos(theta)
        axisY = circleRadius * math.sin(theta)
        coordinates.append((axisX, axisY))

    # Print the coordinates
    for index, (axisX, axisY) in enumerate(coordinates):
        print(f"Point {index+1}: ({axisX:.10f}, {axisY:.10f})")
        exportFile.write(str([index + 1,axisX,axisY]) + "\n")

exportFile.close()

print("Successful Execution.")