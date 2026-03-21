from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:

        if h1 is None:
            return h2
        if h2 is None:
            return h1 

        if h1 is None and h2 is None:
            return h1
        
        head = None 
        curr = None 

        # compare the value and adjust the pointers 
        while h1 and h2:
            # very first node 
            if head is None:
                if h1.val < h2.val:
                    head = h1
                    curr = head 
                    h1 = h1.next 
                else:
                    head = h2 
                    curr = head
                    h2 = h2.next

            else:
                if h1.val < h2.val:
                    curr.next = h1
                    curr = curr.next  # moved to that newly added node.. above 
                    h1 = h1.next 
                else:
                    curr.next = h2
                    curr = curr.next # moved to that newly added node.. above 
                    h2 = h2.next 
        
        # attach whatever left 
        if h1:
            curr.next = h1
        
        # attach whatever left
        if h2:
            curr.next = h2
        
        return head


