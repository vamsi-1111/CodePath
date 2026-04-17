"""
U:
Write a function get village class that takes a integer population
as a parameter. The function returns an integer representing the number 
of digits in population.

Assume that a valid integer for population.

if population = 0 -> returns 1


P:
Iterative:
counter variable
for a loop:
population / 10 => reduce it down by 1 digit and everytime we do that we increment the counter
return counter

Recursive:
base case: if population == 0 -> return 
population / 10
return 1 + get_village_class_iterative()

"""

def get_village_class_iterative(population):
    counter = 0
    if population == 0:
        return 1
    while population != 0:
        population = population // 10
        counter = counter + 1
    
    return counter

def get_village_class_recursive(population):
    if population < 10:
        return 1
    return 1 + get_village_class_recursive(population // 10)

print(get_village_class_recursive(432))
print(get_village_class_iterative(432))
print(get_village_class_recursive(0))

#---------------------------------------------------------------------------------------------------------------------------------------
"""
U: 

    Input: list of lists, walls
    Output: integer the nuber of walls (count of lists)
    assume we dont have a ase where one list contains multiple strings -
    only none or 1 string plus list
    edgecase: an empty list returns 1

    P:
    Base case: When the list is empty
    any time we reach an empty list this means we have finished traversing the list
    return 1
    
    return 1 + count_walls(walls[1:])

"""

def count_walls(walls):
    if walls == []:
         return 1
    return 1 + count_walls(walls[1]) # we dont need slicing we just pass the next list at index 1
                                                                 
# did that work?
# we are getting 1 and 1 
# yes we got 4 and 1
# its because the list is nested. we would use the slicing if it were like ["a", "b", "c"]

walls = ["outer", ["inner", ["keep", []]]]
print(count_walls(walls))
print(count_walls([]))
