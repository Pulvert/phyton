"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method."""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} have {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


class IceCreamSt(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


icecream = IceCreamSt("Iceland", "Icecreams", ["Banana", "Lemon", "Orange"])

icecream.show_flavors()
print(icecream.restaurant_name)


"""9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""

class User:
    def __init__(self, first_name, last_name, id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, nº ID: {self.id}, Years Old: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name}!, welcome to our community")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges2(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, id, age):
         super().__init__(first_name, last_name, id, age)
         self.priv = Privileges()

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


admin = Admin("Juan", "Gallego", 1, 45)
"""admin.show_privileges()""" # Cambiado por ejercicio 9-8

"""9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges."""

new_admin = Admin("Pedro", "Garcia", 2, 41)

new_admin.priv.show_privileges2()


"""9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 65 if it isn’t already. Make
an electric car with a default battery size, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase in the car’s range."""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

tesla = ElectricCar("Tesla", "ne2", 2025)

b = Battery()
b.get_range()
b.upgrade_battery()
b.get_range()