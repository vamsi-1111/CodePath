#hi!

#for player1 and each opponent, find average of placements from races
#compare player1's placement to all opponents to find where player1 belongs
#
class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        averages = []
        n = len(self.race_outcomes)
        player1avg = sum(self.race_outcomes)/n

        for player in opponents:
            averages.append(sum(player.race_outcomes)/n)

        averages.append(player1avg)
        
        averages.sort()

        index = averages.index(player1avg) + 1

        return index
        

# player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
# player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
# player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

# opponents = [player2, player3]
# print(player1.get_tournament_place(opponents))

#shy_guy -> diddy_kong -> dry_bones to shy_guy -> link -> diddy_kong -> toad -> dry_bones

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

shy_guy = Node("Shy Guy")
diddy_kong = Node("Diddy Kong")
dry_bones = Node("Dry Bones")
shy_guy.next = diddy_kong
diddy_kong.next = dry_bones

# Add code to update the list here

link = Node("Link")
toad = Node("Toad")

shy_guy.next = link
link.next = diddy_kong
diddy_kong.next = toad
toad.next = dry_bones


def add_second(head, val):
    nexty = head.next
    valNode = Node(val)
    head.next = valNode
    valNode.next = nexty
    return head



# original_list_head = Node("banana")
# second = Node("blue shell")
# third = Node("bullet bill")
# original_list_head.next = second
# second.next = third


# # Linked list: "banana" -> "blue shell" -> "bullet bill"
# new_list = add_second(original_list_head, "red shell")
# print_linked_list(new_list)

# print("Current List:")
# print_linked_list(shy_guy)


def increment_ll(head):
    current = head
    while current is not None:
        current.value = current.value + 1
        current = current.next
    return head

# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(increment_ll(node_one))

#input = head of linked list
#head of the new list
#edgecases - no head
#if no head ->> return None
#else: head of new linkedlist = copy of head of original
#loop through items in linkedlist, make new node out of original ones that are pointed to by a curr node

#     def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

def copy_ll(head):
    if not head:
        return None
    
    new_head = Node(0)
    temp = new_head
    orig_head = head

    while head:
        temp.next = Node(head.value)
        temp = temp.next
        head = head.next
    
    return new_head.next
    


# mario = Node("Mario")
# daisy = Node("Daisy")
# luigi = Node("Luigi")
# mario.next = daisy
# daisy.next = luigi

# # Linked List: Mario -> Daisy -> Luigi
# copy = copy_ll(mario)

# # Change original list -- should not affect the copy
# mario.value = "Original Mario"

# print_linked_list(mario)
# print_linked_list(copy)
# 
# input: head, n (number of finishers to look at) 
#output: list of top n finishers
#iterating through linked list with counter, adding items into list until we hit n items

def top_n_finishers(head, n):
    top_finishers = []
    count = 0
    curr = head
    while curr and count < n:
        top_finishers.append(curr.value)
        count += 1
        curr = curr.next

    return top_finishers


# head = Node("Daisy", Node("Mario", Node("Toad", Node("Yoshi"))))

# # Linked List: Daisy -> Mario -> Toad -> Yoshi
# print(top_n_finishers(head, 3))

# # Linked List: Daisy -> Mario -> Toad -> Yoshi
# print(top_n_finishers(head, 5))

#input: head, racer -> to be removed
#output: head
#edgecases - no head -> return None, racer not existing -- >same list

def remove_racer(head, racer):
    if not head:
        return None
    
    if head.value == racer:
        head = head.next
        return head

    temp = head
    prev = None
    while temp:
        if temp.value == racer:
            prev.next = temp.next
            return head

        prev = temp
        temp = temp.next
    
    return head





head = Node("Daisy", Node("Mario", Node("Toad", Node("Mario"))))

# Linked List: Daisy -> Mario -> Toad -> Mario
print_linked_list(remove_racer(head, "Mario"))

head = Node("Daisy", Node("Mario", Node("Toad", Node("Mario"))))

# Linked List: Daisy -> Mario -> Toad
print_linked_list(remove_racer(head, "Yoshi"))
