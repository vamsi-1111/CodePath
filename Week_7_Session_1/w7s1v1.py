def count_suits_iterative(suits):
    counter = 0
    for suit in suits:
        counter = counter + 1
    return counter

def count_suits_recursive(suits):
    counter = 1
    if suits == []:
        return 0
    return counter + count_suits_iterative(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

#---------------------------------------------------------------------------------------------------------------------------------------

def sum_stones(stones):
    if stones == []:
        return 0
    return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

#---------------------------------------------------------------------------------------------------------------------------------------

def count_suits_iterative(suits):
    s = set()

    for suit in suits:
        s.add(suit)

    return len(s)

def count_suits_recursive(suits):
    counter = 1
    s = set()
    s.add(suits[0])

    def recursion_helper(suits):
        if suits == []:
            return 0
        if suits[0] in s:
            return 0 + recursion_helper(suits[1:])
        else:
            s.add(suits[0])
            return 1 + recursion_helper(suits[1:])
    
    return counter + recursion_helper(suits[1:])

print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

