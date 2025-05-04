from prueba import Restaurant
from prueba import User, Privileges, Admin

"""9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly."""

vip = Restaurant("Vips", "Mix")

vip.describe_restaurant()

"""9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
the classes User, Privileges, and Admin in one module. Create a separate file,
make an Admin instance, and call show_privileges() to show that everything is
working correctly."""

admin3 = Admin("Jose","Sanz", 5, 23)

admin3.priv.show_privileges2()