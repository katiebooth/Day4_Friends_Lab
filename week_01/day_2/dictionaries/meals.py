# empty_dictionary = {} 

#creat a dictionary of meals
meals = {
    "breakfast" : "youghurt",
    "lunch" : "roll",
    "dinner" : "steak"
}

#Print the meals list for lunch only
print(meals["lunch"])

#Does supper exist
print("supper" in meals)

#Append lunch to pizza instead of roll
meals["lunch"] = "pizza"
print(meals)

meals["supper"] = "beer"

del(meals["breakfast"])
print(meals)

meals["breakfast"] = "porridge"
print(meals)

#List keys (or values)
print(list(meals.keys()))