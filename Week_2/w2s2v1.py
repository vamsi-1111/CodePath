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

def distinct_averages(species_populations):
    my_dict = {}
    while species_populations:
      max_value = max(species_populations)
      min_value = min(species_populations)
      species_populations.remove(max_value)
      species_populations.remove(min_value)
      average = (max_value + min_value) / (2)
      my_dict[average] = my_dict.get(average, 0) + 1

    return len(my_dict)


species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def max_species_copies(raised_species, target_species):
    my_dict = {}
    res = []
    for species in raised_species:
        my_dict[species] = my_dict.get(species, 0) + 1
    for species in target_species:
        if species in my_dict:
            value = my_dict.get(species)
            res.append(value)

    return min(res)

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def count_unique_species(ecosystem_data):
    ptr = 0
    ptr2 = 0
    my_set = set()

    while ptr < len(ecosystem_data):
        if ecosystem_data[ptr2].isdigit():
            num = []
            while ptr2 < len(ecosystem_data) and ecosystem_data[ptr2].isdigit():
                num.append(ecosystem_data[ptr2])
                ptr2 = ptr2 + 1
            ptr = ptr2
            my_set.add(int("".join(num)))
        else:
            ptr = ptr + 1
            ptr2 = ptr

    return len(my_set)

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))