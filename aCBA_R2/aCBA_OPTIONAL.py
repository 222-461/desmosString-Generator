# Automated Coordinate-Based Art - Step OPTIONAL (3)

# Constants

FILEINPUT = "aCBA_coordinateExport.txt"
FILEOUTPUT = "aCBA_coordinateReflect.txt"

# Variables

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

def importData(file_path):
    with open(file_path, "r") as coordinateList:
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

def exportData(file_path, coordinates):

    with open(file_path, "w") as coordinateList:
        for i in range(0, len(coordinates), 2):
            # Write pairs of points as lines
            point1 = coordinates[i]
            point2 = coordinates[i + 1]
            coordinateList.write(f"({point1[0]},{point1[1]}),({point2[0]},{point2[1]})\n")

# Main Program


# Read the original coordinates
coordinates = importData(FILEINPUT)
    
# Get reflection axis
axis = input("Reflect over X-axis or Y-axis? (x/y): ").strip().lower()
    
if axis == "x":
    coordinateReflected = [axisXReflection(point) for point in coordinates]
elif axis == "y":
    coordinateReflected = [axisYReflection(point) for point in coordinates]
else:
    print("Invalid input. Please enter x or y.")
    
# Export reflected coordinates
exportData(FILEOUTPUT, coordinateReflected)
    
print("Successful Execution.")
