"""8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time."""

def sandwichs(*toppings):
    for topping in toppings:
        print(topping)



sandwichs("Cheese", "Vegetal", "York")
sandwichs("Cheese", "York")
sandwichs("York")

"""8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you."""

def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')


diego_profile = build_profile("Diego", "Serrano", age=41, sons=3, city="Madrid")
print(user_profile)
print(diego_profile)

"""8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly."""

def make_car(manufacturer, model_name, **kwargs):
    kwargs["Manufacturer"]=manufacturer
    kwargs["Model Name"]=model_name
    return kwargs


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)


