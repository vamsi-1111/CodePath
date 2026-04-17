class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    ptr1 = clues
    ptr2 = clues.next

    while ptr1 is not ptr2:
        if ptr2.next is None:
            return False
        ptr2 = ptr2.next

    return True
    

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

#---------------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    slow = evidence
    fast = evidence 
    res = []
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            has_cycle = True
            break
        
    if not has_cycle:
        return res

    ptr1 = slow
    ptr2 = slow.next
    res.append(ptr1.value)

    while ptr2 is not ptr1:
        res.append(ptr2.value)
        ptr2 = ptr2.next

    return res

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

#---------------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    high_dummy = Node(0)
    low_dummy = Node(0)

    high = high_dummy
    low = low_dummy

    current = suspect_ratings

    while current:
        if current.value > threshold:
            high.next = current
            high = high.next
        if current.value <= threshold:
            low.next = current
            low = low.next
        current = current.next

    low.next = None
    high.next = low_dummy.next
        
    return high_dummy.next
        
#---------------------------------------------------------------------------------------------------------------------------------------

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print_linked_list(partition(suspect_ratings, 3))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_timelines(known_timeline, witness_timeline):
    result = Node(0)
    res = result
    ptr1 = known_timeline
    ptr2 = witness_timeline

    while ptr1 and ptr2:
        if ptr1.value <= ptr2.value:
            res.next = ptr1
            ptr1 = ptr1.next
        else:
            res.next = ptr2
            ptr2 = ptr2.next
        res = res.next

        if ptr1:
            res.next = ptr1

        if ptr2:
            res.next = ptr2

    return result.next

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))

#---------------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def rotate_right(evidence, k):
    length = 0
    current = evidence
    while current:
        length = length + 1
        current = current.next

    ptr1 = evidence
    ptr2 = evidence
    value = (length - k) % length

    while ptr2.next is not None:
        ptr2 = ptr2.next

    ptr2.next = ptr1

    while value != 0:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        value = value - 1

    ptr2.next = None
    return ptr1

evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))

#---------------------------------------------------------------------------------------------------------------------------------------

def __init__(self, value, next=None):
    self.value = value
    self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_two_numbers(head_a, head_b):
    result = Node(0)
    res = result
    ptr1 = head_a
    ptr2 = head_b
    remainder = 0

    while ptr1 is not None and ptr2 is not None:
        sum = ptr1.value + ptr2.value + remainder
        remainder = sum // 10
        sum = sum % 10
        res.next = Node(sum)
        res = res.next
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    if remainder != 0:
        res.next = Node(remainder)
        res = res.next

    return result.next

head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))