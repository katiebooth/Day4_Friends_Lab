# Ask user for favourite animal - assign animal to variable 
animal = input("What animal are you?")

# force to lower case to avoid incorrect bool 

# check animal is a chicken 
# is_it_a_chicken = animal == "chicken" 

# if true print favourite animal, if kiten say I love kittens! else print not my favourite
if animal == "chicken":
    print ("This is my favourite animal!")
elif animal == "kitten":
        print(f"I love {animal}s!!!")
else:
    print (f"{animal} is not my favourite animal!  Sad...") 
    