##Mary Szemak
##CIS 245
##Assignment 8.1

class Vehicle:

    def __init__(self, _make, _model, _color, _fuelType, _options):
        self.make = _make
        self.model = _model
        self.color = _color
        self.fuelType = _fuelType
        self.options = _options
    

    def GetMake(self):
        return self.make

    def GetModel(self):
        return self.model
    
    def GetColor(self):
        return self.color
    
    def GetFuelType(self):
        return self.fuelType

    def GetOptions(self):
        return self.options

    def ToString(self):
        return "Define this function in the child classes"


class Car(Vehicle):

    def __init__(self, _make, _model, _color, _fuelType,
                _options, _engineSize, _numDoors):
        Vehicle.__init__(self, _make, _model, _color, _fuelType, _options)
        self.engineSize = _engineSize
        self.numDoors = _numDoors

    def GetEngineSize(self):
        return self.engineSize

    def GetNumDoors(self):
        return self.numDoors

    def ToString(self):
        txt = "Vehicle Type: Car\n{Make} {Model}\nColor: {Color}\nFuel Type: {FuelType}\n"
        txt = txt + "Engine Size: {EngineSize}\nNumber of Doors: {NumDoors}\nOptions: "

        for option in self.options:
            txt = txt + option + ", "

        end = int(len(txt) - 2)
        txt = txt[0:end]
        
        txt = txt.format(Make = self.make, Model = self.model, Color = self.color,
                         FuelType = self.fuelType, EngineSize = self.engineSize,
                         NumDoors = self.numDoors)
        return txt

        

class Pickup(Vehicle):

    def __init__(self, _make, _model, _color, _fuelType,
               _options, _cabStyle, _bedLength):
        Vehicle.__init__(self, _make, _model, _color, _fuelType, _options)
        self.cabStyle = _cabStyle
        self.bedLength = _bedLength

    def GetCabStyle(self):
        return self.cabStyle

    def GetBedLength(self):
        return self.bedLength

    def ToString(self):
        txt = "Vehicle Type: Pickup\n{Make} {Model}\nColor: {Color}\nFuel Type: {FuelType}\n"
        txt = txt + "Cab Style: {CabStyle}\nBedLenth: {BedLength}\nOptions: "

        for option in self.options:
            txt = txt + option + ", "
            
        end = int(len(txt) - 2)
        txt = txt[0:end]
        
        txt = txt.format(Make = self.make, Model = self.model, Color = self.color,
                         FuelType = self.fuelType, CabStyle = self.cabStyle,
                         BedLength = self.bedLength)
        return txt

OPTIONS = ["Keyless Entry", "Remote Start", "Fog Lights", "Power Mirrors",
           "Power Seats", "Bluetooth", "GPS", "Collision Detection"]

def GetOptions(_OPTIONS):
    selection = -1
    options = []
    index = 1
    validInput = True

    txt = ""
    for o in _OPTIONS:
        txt = txt + str(index) + ") " + o + "\n"
        index += 1

    txt = txt + "0) Done"

    index = 0
    
    while (True):
        validInput = True
        
        print("\n\nSelect an Option.")
        print(txt)
        
        try:
            selection = int(input())
        except:
            print("Invalid Input.\nPlease enter an integer between 0 and "  + str(len(_OPTIONS)) + ".")
            validInput = False

        if (selection < 0) or (selection > len(_OPTIONS)):
            print("Invalid Input.\nPlease enter an integer between 0 and "  + str(len(_OPTIONS)) + ".")
            validInput = False
            
        if (validInput):
            if (selection == 0):
                break
            
            elif _OPTIONS[selection - 1] not in options:
                options.append(_OPTIONS[selection - 1]) 

            else:
                print("Option alread selected")

    if len(options) == 0:
        options.append("None")

    return options

print("Welcome to Mary's Virtual Garage\n\n")

print("Please create a car.")
print("Enter the make.")
make = input()

print("Enter the model.")
model = input()

print("Enter the color.")
color = input()

print("Enter the fuel type.")
fuelType = input()

print("Enter the engine size.")
engineSize = input()

print("Enter the number of doors.")
numDoors = input()

options = GetOptions(OPTIONS)

car = Car(make, model, color, fuelType, options, engineSize, numDoors)

##truck

print("Please create a Pickup.")
print("Enter the make.")
make = input()

print("Enter the model.")
model = input()

print("Enter the color.")
color = input()

print("Enter the fuel type.")
fuelType = input()

print("Enter the cab style.")
cabStyle = input()

print("Enter the bed length.")
bedLength = input()

options = GetOptions(OPTIONS)

pickup = Pickup(make, model, color, fuelType, options, cabStyle, bedLength)

print("\n\n")
print(car.ToString())

print("\n\n")
print(pickup.ToString())
    
        
        
