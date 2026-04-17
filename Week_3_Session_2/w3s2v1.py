from collections import deque

def manage_stage_changes(changes):
    res = []
    cancelled = []
    for change in changes:
        if "Schedule" in change:
            temp = change.replace("Schedule ", "")
            res.append(temp)
        elif change == "Cancel":
            temp = res.pop()
            cancelled.append(temp)
        elif change == "Reschedule":
            temp = cancelled.pop()
            res.append(temp)
    return res

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))

import queue


def process_performance_requests(requests):
    pq = queue.PriorityQueue()
    for request in requests:
        pq.put(request)
    res = []
    while not pq.empty():
        temp = pq.get()
        res.append(temp[1])
    return res[::-1]

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

def collect_festival_points(points):
    stack = []
    res = 0
    for point in points:
        stack.append(point)
    while stack:
        res = res + stack.pop()
    return res

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 



def booth_navigation(clues):
    stack = []
    for clue in clues:
        if clue != "back":
            stack.append(clue)
        else:
            if stack:
                stack.pop()
    return stack


clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

def merge_schedules(schedule1, schedule2):
    queue1 = deque(schedule1)
    queue2 = deque(schedule2)
    res = ""

    while queue1 and queue2:
        res += queue1.popleft()
        res += queue2.popleft()
    while queue1:
        res += queue1.popleft()
    while queue2:
        res += queue2.popleft()
    return res 

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 

#Monotonic stack & dictionary 
#Iterate through schedule2 & add items to stack & pop out items when a larger item comes & add to the hashmap the item and its next largest value
#Iterate through schedule1 and then obtain the values accordingly
def next_greater_event(schedule1, schedule2):
    next_greater = {}
    stack = []
    stack.append(schedule2[0])

    for num in schedule2: 
        while stack and num > stack[-1]: #stack is not empty and the last item on the stack is larger than num
            prev = stack.pop() #if it is then we can pop the last item
            next_greater[prev] = num #say this items next largest value is num
        stack.append(num) #we append num to the list
    while stack: #stack is not empty for all remaining elements that we could not find the next largest number for
        prev = stack.pop() #we pop the item and then say it is responsible for returning -1
        next_greater[prev] = -1

    return [next_greater[num] for num in schedule1] #builds a list by taking the key nums and finding its value for all values in schedule1

#What to learn: 
# - Monotonic Stacks means that we add items to the stack till we find the next greater value 
# - Once next greatest value is found we can just pop the item on the stack and append the new greater value
# - We keep doing this till we iterate through the entire list
# - Throughout this process when we pop items we add it to the hashmap so we know what the next greatest value is for each item
# - All remaining values we add -1 to the hashmap
print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4]))

def sort_performances_by_type(performances):
    even_stack = []
    odd_stack = []
    res = []
    for performance in performances:
        if performance % 2 == 0:
            even_stack.append(performance)
        if performance % 2 == 1:
            odd_stack.append(performance)

    while even_stack:
        res.append(even_stack.pop())

    while odd_stack:
        res.append(odd_stack.pop())

    return res

print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0])) 

