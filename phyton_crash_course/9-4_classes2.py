"""9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
Add an attribute called number_served with a default value of 0. Create an 
instance called restaurant from this class. Print the number of customers the 
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business."""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} have {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def increment_number_served(self):
        self.number_served += 100


restaurant = Restaurant("Vips", "Mix")


print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.increment_number_served()
print(restaurant.number_served)


"""9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0."""

class User:
    def __init__(self, first_name, last_name, id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, nº ID: {self.id}, Years Old: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name}!, welcome to our community")

    def increment_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attemps(self):
        self.login_attempts = 0

diego = User("Diego", "Serrano", 1, 41)

print(diego.login_attempts)
diego.increment_login_attemps()
diego.increment_login_attemps()
diego.increment_login_attemps()
diego.increment_login_attemps()
print(diego.login_attempts)
diego.reset_login_attemps()
print(diego.login_attempts)