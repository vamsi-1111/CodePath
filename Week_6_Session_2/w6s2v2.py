class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def trail_length(trailhead):

    ptr1 = trailhead
    if not trailhead:
        return 0

    ptr1 = ptr1.next
    count = 1

    while ptr1 != trailhead:
        ptr1 = ptr1.next
        count = count + 1

    return count

marker1 = Node("Marker 1")
marker2 = Node("Marker 2")
marker3 = Node("Marker 3")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker1

print(trail_length(marker1))

#---------------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def clear_trail(trailhead):
    ptr1 = trailhead
    ptr2 = trailhead
    s = set()

    while ptr1:
        s.add(ptr1)
        if ptr1.next in s:
            break
        else:
            ptr1 = ptr1.next

    ptr1.next = None
    ptr1 = ptr1.next

    return ptr2

marker1 = Node("Trailhead")
marker2 = Node("Trail Fork")
marker3 = Node("The Falls")
marker4 = Node("Peak")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker4
marker4.next = marker2

print_linked_list(clear_trail(marker1))

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

def remove_duplicate_markers(trailhead):
    temp_head = Node(0)
    temp_head.next = trailhead

    ptr1 = temp_head
    ptr2 = trailhead

    while ptr2:
        if ptr2.next and ptr2.value == ptr2.next.value:
            value = ptr2.value
            while ptr2 and ptr2.value == value:
                ptr2 = ptr2.next

            ptr1.next = ptr2
        else:
            ptr1 = ptr2
            ptr2 = ptr2.next
    
    return temp_head.next

trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print_linked_list(remove_duplicate_markers(trailhead))

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

def selective_trail_clearing(trailhead, m, n):
    temp = Node(0)
    temp.next = trailhead
    ptr1 = temp

    while ptr1:
        for i in range(m):
            if ptr1 is None:
                return temp.next
            ptr1 = ptr1.next
        ptr2 = ptr1
        for i in range(n):
            if ptr2 is None:
                return temp.next
            ptr2 = ptr2.next
        ptr1.next = ptr2.next

    return temp.next

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12))))))))))))
print_linked_list(selective_trail_clearing(trailhead, 2, 3))

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

def locate_cache(cache_labels):
    value = 0
    array = []
    ptr1 = cache_labels

    while ptr1:
       array.append(ptr1.value)
       ptr1 = ptr1.next

    power_value = len(array) - 1

    for num in array:
        value = value + (num * (2 ** power_value))
        power_value = power_value - 1

    return value

cache_labels = Node(1, Node(0, Node(1))) 
print(locate_cache(cache_labels))

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

def merge_trail(trailhead):
    temp = Node(0)
    ptr1 = temp
    ptr2 = trailhead


    while ptr2:
        value = 0
        while ptr2 and ptr2.value == 0:
            ptr2 = ptr2.next
            if ptr2 is None:
                return temp.next
        while ptr2 and ptr2.value != 0:
            value = value + ptr2.value
            ptr2 = ptr2.next
        ptr1.next = Node(value)
        ptr1 = ptr1.next

    return temp.next

trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(2, Node(0))))))))
trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

print_linked_list(merge_trail(trail1))
print_linked_list(merge_trail(trail2))