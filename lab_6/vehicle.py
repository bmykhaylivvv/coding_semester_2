'''
Module for representing different types of vehicle.
'''


class Vehicle:
    '''
    Represents a vehicle.
    '''

    def __init__(self, brand, model, vehicle_type, tank_capacity=0, fuel_consumption=6):
        self.brand = brand
        self.model = model
        self.vehicle_type = vehicle_type
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.fuel_level = 0

    def __str__(self):
        return f'Vehicle {self.brand} {self.model} is a {self.vehicle_type}.\
 It has a gas tank size of {self.tank_capacity}.'

    def fuel_up(self, fuel_amount):
        '''
        Fills the tank.
        '''
        self.fuel_level += fuel_amount
        return 'Gas tank is filled.'

    def get_fuel_level(self):
        '''
        Returns fuel level.
        '''
        return self.fuel_level

    def drive(self, distance):
        '''
        Simulates driving.
        '''
        self.current_fuel_level = self.fuel_level - \
            int((distance/100)) * self.fuel_consumption
        self.fuel_level = self.current_fuel_level
        if self.current_fuel_level > 0:
            return f'The {self.brand} {self.model} is now driving.'

        return 'Not enough fuel level in a gas tank.'


class ElectricVehicle(Vehicle):
    '''
    Represents an electric vehicle.
    '''

    def __init__(self, brand, model, vehicle_type):
        super().__init__(brand, model, vehicle_type)
        self.charge_level = 0
        self.battery = Battery()

    def __str__(self):
        return f'Vehicle {self.brand} {self.model} is a {self.vehicle_type}.'

    def charge(self):
        '''
        Simulates car charging.
        '''
        self.charge_level = 100
        self.battery.current_charge = 100
        return 'The vehicle is fully charged.'

    def get_charge_level(self):
        '''
        Returns car charge level.
        '''
        return self.charge_level

    def drive(self):
        self.charge_level = 0
        self.battery.current_charge = 0
        return f'The {self.brand} {self.model} is now driving.'

    def get_battery_info(self):
        '''
        Returns batery info.
        '''
        return f'Battery has size of {self.battery.size}, it is charged up to \
{self.battery.current_charge}%'


class Battery:
    '''
    Represents a batterry of electric vehicle.
    '''

    def __init__(self, current_charge=0):
        self.current_charge = current_charge
        self.size = 85


def test_vehicle():
    """
    Test function
    """
    print("Testing Vehicle classes...")
    # A basic Vehicle has a brand, model, type, volume of gas_tank_size
    # fuel_level that by default equals 0 and fuel_consumption
    # that by default equals 6. It can drive and be fueled up
    vehicle = Vehicle("Subaru", "Forester", "Crossover", 16, 7)
    assert (type(vehicle) == Vehicle)
    assert (isinstance(vehicle, Vehicle))
    assert (str(vehicle) ==
            "Vehicle Subaru Forester is a Crossover. It has a gas tank size of 16.")

    # change some attributes
    assert (vehicle.fuel_up(12) == "Gas tank is filled.")
    assert (vehicle.get_fuel_level() == 12)
    # When vehicle drives, it uses the fuel level
    # Vehicle uses fuel in amount of
    # fuel_consumption * distance to drive / 100
    assert (vehicle.drive(100) == "The Subaru Forester is now driving.")
    # the vehicle travelled 100 km and the fuel level reduced
    # from 12 to 5
    assert (vehicle.get_fuel_level() == 5)
    assert (vehicle.drive(100) == "Not enough fuel level in a gas tank.")

    # ElectricVehicle is a Vehicle that doesn't need a gas_tank_size
    # and doesn't have a fuel_consumption.
    # You can charge and drive it.
    electric_vehicle = ElectricVehicle('Tesla', 'Model 3', 'Sedan')
    assert (type(electric_vehicle) == ElectricVehicle)
    assert (isinstance(electric_vehicle, ElectricVehicle))
    assert (isinstance(electric_vehicle, Vehicle))
    assert (str(electric_vehicle) == "Vehicle Tesla Model 3 is a Sedan.")

    assert (electric_vehicle.get_fuel_level() == 0)
    assert (electric_vehicle.charge() == "The vehicle is fully charged.")
    assert (electric_vehicle.get_charge_level() == 100)
    assert (electric_vehicle.drive() == "The Tesla Model 3 is now driving.")
    assert (electric_vehicle.get_charge_level() == 0)

    # the attribute battery has to belong to Battery class
    # the Battery has a size, that by default equals 85
    # and charge level that by default equals 0
    assert (type(electric_vehicle.battery) == Battery)
    assert (isinstance(electric_vehicle.battery, Battery))
    assert (electric_vehicle.get_battery_info() ==
            "Battery has size of 85, it is charged up to 0%")

    print("Done!")


if __name__ == '__main__':
    test_vehicle()
