"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two 
attributes individually, and then call both methods."""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} have {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

vips = Restaurant("Vips", "Mix")

vips.describe_restaurant()
vips.open_restaurant()


"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance."""

chinese = Restaurant("Hao Kin", "Chinese")
thay = Restaurant("Delhi", "Thay")
alterntiva = Restaurant("Alternativa", "Daily Menu")

chinese.describe_restaurant()
thay.describe_restaurant()
alterntiva.describe_restaurant()

"""9-3. Users: Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both
methods for each user."""

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

diego = User("Diego", "Serrano", 1, 41)

diego.describe_user()
diego.greet_user()        
