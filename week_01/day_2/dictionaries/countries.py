from itertools import count


countries = {
    "uk" : {
        "capital" : "London",
        "population" : 60000000
    },
    "germany" : {
        "capital" : "Berlin",
        "population" : 80000000
    }
}

#Print just the Germany population (Germany is it's own dictionary as is UK)
print(countries["germany"]["population"])