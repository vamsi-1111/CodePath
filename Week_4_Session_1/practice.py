class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    ptr1 = 0
    ptr2 = 1
    while ptr2:
        ptr1 = ptr2.next
        


    
    pass

#plan: iterate through the linked list until the pointer turns to null and then we take the current poisition of the pointer and connect it back to the node that comes before it