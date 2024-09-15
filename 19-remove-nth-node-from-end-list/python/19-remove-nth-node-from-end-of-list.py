# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """Singly-linked list definition
        """
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """dummy node is created and points to the head of the list
        """
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    return elements
