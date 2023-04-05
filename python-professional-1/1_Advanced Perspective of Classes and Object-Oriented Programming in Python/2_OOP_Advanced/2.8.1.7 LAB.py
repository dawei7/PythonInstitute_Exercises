"""
Estimated time
45 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in operating with inheritance and composition
Scenario
Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.

Your task is to :

define classes representing:
tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
engine; methods available: start(), stop(), get_state(); attribute available: fuel type
vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN
based on the classes defined above, create the following objects:
two sets of tires: city tires (size: 15), off-road tires (size: 18)
two engines: electric engine, petrol engine
instantiate two objects representing cars:
the first one is a city car, built of an electric engine and city tires
the second one is an all-terrain car build of a petrol engine and off-road tires
play with the cars by calling methods responsible for interaction with components.
"""

class Tires():

    def __init__(self,size):
        self.size = size

    def get_pressure(self):
        print("The pressure is 3 bar.")

    def pump(self):
        print("Pumping tires.")

class Engine():
    
    def __init__(self,fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Starting.")

    def stop(self):
        print("Stopping.")

    def get_state(self):
        print("Getting State.")


class Vehicle():
    
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

    
# two sets of tires: city tires (size: 15), off-road tires (size: 18)
city_tires = Tires(15)
off_road_tires = Tires(18)

# two engines: electric engine, petrol engine
electric_engine = Engine("Electric")
petrol_engine = Engine("Petrol")

#the first one is a city car, built of an electric engine and city tires
my_vehicle_1 = Vehicle("1",electric_engine,city_tires)
print(my_vehicle_1.engine.fuel_type)
print(my_vehicle_1.VIN)
my_vehicle_1.engine.start()
my_vehicle_1.engine.stop()
my_vehicle_1.engine.get_state()
print(my_vehicle_1.tires.size)
my_vehicle_1.tires.get_pressure()
my_vehicle_1.tires.pump()


# the second one is an all-terrain car build of a petrol engine and off-road tires
my_vehicle_2 = Vehicle("2",petrol_engine,off_road_tires)
print(my_vehicle_2.engine.fuel_type)
print(my_vehicle_2.VIN)
my_vehicle_2.engine.start()
my_vehicle_2.engine.stop()
my_vehicle_2.engine.get_state()
print(my_vehicle_2.tires.size)
my_vehicle_2.tires.get_pressure()
my_vehicle_2.tires.pump()




