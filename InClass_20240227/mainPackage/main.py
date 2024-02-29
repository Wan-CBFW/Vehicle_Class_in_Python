#main.py
from vehiclePackage.vehicleClass import *
from vehiclePackage.hybridClass import Hybrid


if __name__ == "__main__":
    # Instantiate an object of type hybrid
    myPrius = Hybrid("Hybrid", "Toyota", "Prius", 220)
    # Invoke the printType method using the Hybrid object we just created
    myPrius.printType()
    '''
    # Instantiate an object if type vehicle
    myCorvette = Vehicle("Car", 120)  #Trigger a call to constructor
    myCorvette.printType()      #invoke the method on the object
    
    # Invoke the getter for maximum speed, store the return value in a variable 
    # print that to the console
    
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed: ", maximum_speed)
    
    # instantiate another vehicle object . You can name it
    myTank = Vehicle("Tank")    #myTank is an object of type vehicle
    
    # I want a list of 3 vehicles:Car,Boat, Space ship
    # You can pick the names and properties
    # I want some friendly output to demo your work
    
    
    myVehicles = [Vehicle("Cobalt", 100), Vehicle("Yacht", 30), Vehicle("Vroom", 2000)]
    # iterate over the list
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
    '''
    