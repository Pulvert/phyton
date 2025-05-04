"""8-15. Printing Models: Put the functions for the example printing_models.py in a 
separate file called printing_functions.py. Write an import statement at the top 
of printing_models.py, and modify the file to use the imported functions."""


# Importo el 8-12, pero al tener números lo tengo que hacer así:

import importlib

module = importlib.import_module("8-12_functions5")
module.sandwichs("Cheese", "Vegetal", "York")

"""8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *"""




"""8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section."""
