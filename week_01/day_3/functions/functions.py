# def greet(name, age):
#     return "Hello " + name + " you are " + age

# name = "Steven"
# age = "47"

# greeting = greet(name, age)
# print(greeting)


chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]
def get_total_eggs(list):
    total_eggs = 0
    
    for bird in list:
        total_eggs += bird["eggs"]
    
    return(f"{total_eggs} eggs collected")

print()
print(get_total_eggs(chickens))