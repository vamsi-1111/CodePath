def final_supply_costs(costs):
    #Understand
    #i represents the index number of the supply item
    #costs[i] represents the cost of the supply item
    #j & costs[j] represent the same thing as i & costs[i]
    #for there to be a discount j > i (index wise) && costs[j] < costs[i] (price wise)
    ptr1 = 0
    ptr2 = 1
    res = []
    while ptr1 < len(costs):
        val = None
        while ptr2 < len(costs):
            if(costs[ptr2] <= costs[ptr1]):
                val = costs[ptr1] - costs[ptr2]
                res.append(val)
                break
            elif(costs[ptr2] > costs[ptr1]):
                ptr2 = ptr2 + 1
        if val == None:
            res.append(costs[ptr1])
        elif val != None:  
            val = None
        ptr1 = ptr1 + 1
        ptr2 = ptr1 + 1
    return res

print(final_supply_costs([8, 4, 6, 2, 3])) 
print(final_supply_costs([1, 2, 3, 4, 5])) 
print(final_supply_costs([10, 1, 1, 6]))

def first_symmetrical_landmark(landmarks):

    res = []
    for landmark in landmarks:
        ptr1 = 0
        ptr2 = len(landmark) - 1
        if len(landmark) % 2 == 0:
            while ptr1 < ptr2:
                if landmark[ptr1] == landmark[ptr2]:
                    ptr1 = ptr1 + 1
                    ptr2 = ptr2 - 1
                elif landmark[ptr1] != landmark[ptr2]:
                    break
            if ptr1 > ptr2:
                res.append(landmark)
        elif len(landmark) % 2 == 1:
            while ptr1 != ptr2:
                if landmark[ptr1] == landmark[ptr2]:
                    ptr1 = ptr1 + 1
                    ptr2 = ptr2 - 1
                elif landmark[ptr1] != landmark[ptr2]:
                    break
            if ptr1 == ptr2:
                res.append(landmark)
    return res

print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff"])) 

def terrain_elevation_match(terrain):
  #Understand:
  #I means that this current index is smaller than the next index
  #D means that this current index is larger than the next index
  #Organize it in a list based on the indices
  #The list should follow the proper order of I (smaller than the next) & D (bigger than the next)
  #Problem:
  #Iterate through the string
  #2 pointer method 
  #

  pass