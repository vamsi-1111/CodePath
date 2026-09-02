def most_endangered(species_list):
    population = 100
    my_dict = {}

    for item in species_list:
        if item.get("population") < population:
            my_dict[item.get("population")] = item.get("name")

    return next(reversed(my_dict.values()))

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def count_endangered_species(endangered_species, observed_species):
    my_set = set(endangered_species)
    count = 0

    for item in observed_species:
        if item in my_set:
            count = count + 1

    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def navigate_research_station(station_layout, observations):
    my_dict = {}
    my_set = set(observations)
    prev = 0
    res = 0

    for index, char in enumerate(station_layout):
        if char in my_set:
            my_dict[char] = index
    
    for char in observations:
        if prev == 0:
            value = my_dict.get(char) - 0
            res = res + value
            prev = char
        else:
            value = abs(my_dict.get(char) - my_dict.get(prev))
            res = res + value
            prev = char

    return res


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def prioritize_observations(observed_species, priority_species):
    my_dict = {}
    res2 = []
    res = []
    for species in observed_species:
        if species in priority_species:
            my_dict[species] = my_dict.get(species, 0) + 1
        else:
            res2.append(species)
    for species in priority_species:
        value = my_dict.get(species)
        while value > 0:
            res.append(species)
            value = value - 1

    sorted(res2)
    res.extend(res2)
    return res

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

