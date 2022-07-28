def get_name(person):
    return person["name"]

def get_favourite_tv_show(tv):
    return tv["favourites"]["tv_show"]

def likes_to_eat(person,food):
    for snacks in person["favourites"]["snacks"]:
        if snacks == food:
            return True
    return False

def add_friend(person, name):
    person["friends"].append(name)

def remove_friend(person, name):
    person["friends"].remove(name)

def total_money(person):
    total_cash = 0
    for people in person:
        total_cash += people["monies"]
    return total_cash

def lend_money(person2, person1, amount):
    person2["monies"] = person2["monies"] - amount
    person1["monies"] = person1["monies"] + amount

def all_favourite_foods(people):
    favourite_foods = []
    for person in people:
        favourite_foods += person["favourites"]["snacks"]
    return favourite_foods    
    
      
        