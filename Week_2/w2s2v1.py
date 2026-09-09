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
        if ecosystem_data[ptr].isdigit():
            num = []
            while ptr < len(ecosystem_data) and ecosystem_data[ptr].isdigit():
                num.append(ecosystem_data[ptr])
                ptr = ptr + 1
            my_set.add(int("".join(num)))
        else:
            ptr = ptr + 1

    return len(my_set)

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def num_equiv_species_pairs(species_pairs):
    my_dict = {}
    duplicates = 0
    for pair in species_pairs:
        my_dict[tuple(sorted(pair))] = my_dict.get(tuple(sorted(pair)), 0) + 1

    for value in my_dict.values():
        if value != 1:
            val = value * (value - 1) // 2
            duplicates = duplicates + val

    return duplicates

species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(num_equiv_species_pairs(species_pairs1))
print(num_equiv_species_pairs(species_pairs2))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def remove_low_rated_destinations(destinations, rating_threshold):
    my_dict = {}
    for key, value in destinations.items():
        if value > rating_threshold:
            my_dict[key] = value

    return my_dict

destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def unique_souvenir_counts(souvenirs):
    my_dict = {}
    my_set = set()
    for souvenir in souvenirs:
        my_dict[souvenir] = my_dict.get(souvenir, 0) + 1

    for key, values in my_dict.items():
        if values in my_set:
            return False
        else:
            my_set.add(values)

    return True

souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def decode_message(key, message):
    my_dict = {}
    letter = 'a'
    string = ""
    for char in key:
        if char == " ":
            if char not in my_dict:
                my_dict[char] = " "
            else:
                continue
        else:
            if char not in my_dict:     
                my_dict[char] = letter
                letter = chr(ord(letter) + 1)
            else:
                continue

    for char in message:
        if char in my_dict:
            string = string + my_dict.get(char)


    return string
    
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        frequency[rating] = frequency.get(rating, 0) + 1

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, 
                        frequency[rating] + frequency[rating + 1])  

    return max_length

ratings1 = [1, 3, 2, 2, 5, 2, 3, 7]
ratings2 = [1, 2, 3, 4]
ratings3 = [1, 1, 1, 1]

print(find_longest_harmonious_travel_sequence(ratings1))  # 5
print(find_longest_harmonious_travel_sequence(ratings2))  # 2
print(find_longest_harmonious_travel_sequence(ratings3))  # 0

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def is_route_covered(trips, start_dest, end_dest):
    my_dict = {}
    for arr in trips:
        start_value = arr[0]
        end_value = arr[-1]
        while start_value <= end_value:
            my_dict[start_value] = my_dict.get(start_value, 0) + 1
            start_value = start_value + 1

    if start_dest > end_dest:
        return False

    while start_dest <= end_dest:
        if start_dest in my_dict:
            start_dest = start_dest + 1
        else:
            return False

    return True

trips1 = [[1, 2], [3, 4], [5, 6]]
start_dest1, end_dest1 = 2, 5

trips2 = [[1, 10], [10, 20]]
start_dest2, end_dest2 = 21, 21

trips3 = [[1, 2], [3, 5]]
start_dest3, end_dest3 = 2, 5

print(is_route_covered(trips1, start_dest1, end_dest1))
print(is_route_covered(trips2, start_dest2, end_dest2))
print(is_route_covered(trips3, start_dest3, end_dest3))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def most_popular_even_destination(destinations):
    my_dict = {}
    val = 0
    res = float("inf")
    for destination in destinations:
        my_dict[destination] = my_dict.get(destination, 0) + 1

    for key, value in my_dict.items():
        if value >= val and key % 2 == 0:
            if value == val:
                res = min(res, key)
            elif value > val:
                res = key
                val = value

    if res == float("inf"):
        return -1

    if my_dict.get(res) == 0:
        return -1

    return res 

destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

print(most_popular_even_destination(destinations1))
print(most_popular_even_destination(destinations2))
print(most_popular_even_destination(destinations3))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
