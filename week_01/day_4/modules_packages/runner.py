# import your file to be used within the code

# import calculator

# when calling the function from another file you need to add it within the brackets i.e. calculator.FUNCTION_INSIDE_CALCULATOR_TO_BE_USED
# in this case it's add

# print(calculator.add(10,20))


# OR you can import a specific function

# from calculator import add
# This way you do NOT need to specify the file in the function call
# print(add(10,20))


# you can also import ALL functions using the star - this imports only functions to be used not variables
# from calculator import *
# print(multiply(10,20))

# you can also truncate the name and/or give it an alias as below
# import calculator as calc

# you can also alias function methods in the same way
# from calculator import add as alisname


# importing from files in other directories once they are a "package" - this is denoted by the __init__.py file
from modules.calculator import *
from math import add as math_add

print(add(10,20))
print(multiply(10,5))
print(math_add(5,6))
