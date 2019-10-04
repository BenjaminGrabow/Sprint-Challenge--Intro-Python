# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
class Vehicle: #base class for all classes
  pass

class FlightVehicle(Vehicle): # base class for class Airplane and Starship and child of Vehicle
  pass

class Airplane(FlightVehicle): # child of class FlightVehicle and Grandchild of Vehicle
  pass

class Starship(FlightVehicle): # child of class FlightVehicle and Grandchild of Vehicle
  pass

class GroundVehicle: #base class for class Car and Motorcycle and child of Vehicle
  pass

class Car(GroundVehicle): #Child of class GroundVehicle and Grandchild of Vehicle
  pass

class Motorcycle(GroundVehicle): #Child of class GroundVehicle and Grandchild of Vehicle
  pass
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
