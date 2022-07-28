chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

eggs = 0

# for dictionary in list
for chicken in chickens:
    # Printing more than one value at a time
    print(f'{chicken["name"]} is {chicken["age"]} years old')
    eggs = chicken["eggs"] + eggs

print()
print(f"Total eggs laid: {eggs}")