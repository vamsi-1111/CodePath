def space_crew(crew, position):
    my_dict = {}

    for index, member in enumerate(crew):
        my_dict[member] = position[index]
    
    return my_dict

exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def planet_lookup(planet_name):
    planet_name_value = planetary_info.get(planet_name)
    if planet_name_value is None:
        return "Sorry, I have no data on that planet."
    moons_value = planet_name_value.get("Moons")
    if moons_value is None:
        return "Sorry, I have no data on that planet."
    orbital_period_value = planet_name_value.get("Orbital Period")
    if orbital_period_value is None:
        return "Sorry, I have no data on that planet."

    return "Planet {planet_name_value} has an orbital period of {orbital_period_value} Earth days and has {moons_value} moons."

planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}

print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    list = []
    command_module_value = oxygen_levels.get("Command Module")
    if command_module_value < min_val or command_module_value > max_val:
        list.append("Command Module")
    habitation_module_value = oxygen_levels.get("Habitation Module")
    if habitation_module_value < min_val or habitation_module_value > max_val:
        list.append("Habitation Module")
    laboratory_module_value = oxygen_levels.get("Laboratory Module")
    if laboratory_module_value < min_val or laboratory_module_value > max_val:
        list.append("Laboratory Module")
    airlock_value = oxygen_levels.get("Airlock")
    if airlock_value < min_val or airlock_value > max_val:
        list.append("Airlock")
    storage_bay_value = oxygen_levels.get("Storage Bay")
    if storage_bay_value < min_val or storage_bay_value > max_val:
        list.append("Storage Bay")

    return list

oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def data_difference(experiment1, experiment2):
    dict = {}
    temperature_value_1 = experiment1.get("temperature")
    temperature_value_2 = experiment2.get("temperature")
    if temperature_value_1 != temperature_value_2:
        dict["temperature"] = temperature_value_1
    
    pressure_value_1 = experiment1.get("pressure")
    pressure_value_2 = experiment2.get("pressure")
    if pressure_value_1 != pressure_value_2:
        dict["pressure"] = pressure_value_1

    humidity_value_1 = experiment1.get("humidity")
    humidity_value_2 = experiment2.get("humidity")
    if humidity_value_1 != humidity_value_2:
        dict["humidity"] = humidity_value_1
    
    return dict

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def get_winner(votes):
    dict = {}
    max = -1
    res = None
    for vote in votes:
        if vote in dict:
            dict[vote] = dict.get(vote) + 1
        else:
            dict[vote] = 1
    
    for key in dict.keys():
        if dict.get(key) > max:
            max = dict.get(key)
            res = key
    return res

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def check_if_complete_transmission(transmission):
    """
    :type transmission: str
    :rtype: bool
    """
    dict = {}
    for char in transmission:
        dict[char] = dict.get(char, 0) + 1
    
    if len(dict) == 26:
        return True
    else:
        return False

transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def max_number_of_string_pairs(signals):
    seen = {}
    res = 0

    for s in signals:
        rev = s[::-1]

        if rev in seen:
            res = res + 1
        else:
            seen[s] = True
    
    return res

signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def find_difference(signals1, signals2):
    diff_1 = []
    diff_2 = []
    set_1 = set(signals1)
    set_2 = set(signals2)

    for set1 in set_1:
        if set1 in set_2:
            continue
        else:
            diff_1.append(set1)
    
    for set2 in set_2:
        if set2 in set_1:
            continue
        else:
            diff_2.append(set2)
    
    return diff_1, diff_2

signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3]
signals2_example2 = [1, 1, 2, 2]

print(find_difference(signals1_example1, signals2_example1)) 
print(find_difference(signals1_example2, signals2_example2))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def find_common_signals(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)
    count = 0
    result = []

    for signal in signals1:
        if signal in set2:
            count = count + 1
        else:
            continue
    
    result.append(count)
    count = 0
    
    for signal in signals2:
        if signal in set1:
            count = count + 1
        else:
            continue
    
    result.append(count)

    return result

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def find_common_signals(signals1, signals2):
    my_dict_1 = {}
    my_dict_2 = {}
    result = []

    for signal in signals1:
        my_dict_1[signal] = my_dict_1.get(signal, 0) + 1
    
    for signal in signals2:
        my_dict_2[signal] = my_dict_2.get(signal, 0) + 1

    count = 0
    for signal in signals1:
        if signal in my_dict_2:
            count = count + 1
    
    result.append(count)

    count = 0
    for signal in signals2:
        if signal in my_dict_1:
            count = count + 1
    
    result.append(count)

    return result 


signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] = freq[signal] + 1
        else:
            freq[signal] = 1

    sorted_signals = sorted(signals, key=lambda x: (freq[x], -x))

    return sorted_signals

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1)) 
print(frequency_sort(signals2)) 
print(frequency_sort(signals3))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def find_final_hub(paths):
    my_dict = {}
    for path in paths:
        my_dict[path[0]] = path[1]

    value = next(iter(my_dict.values()))

    while value in my_dict.keys():
        value = my_dict.get(value)

    return value

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))
