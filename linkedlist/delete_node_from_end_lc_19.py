from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute Force Using Twice a Loop 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if (head is None) or (head.next is None and n == 1):
            return None 

        
        count = 0
        curr = head

        while curr:
            curr = curr.next 
            count += 1
        
        # print(count)

        # if we remove head for the input : 1--> 2 --> None and n = 2 
        if n == count:
            return head.next 
        
        prev_count = count - n -1 # -1 because we have aleady .. at the 1st node 
        prev = head
        # print(f"Prev count is : {prev_count}")
        for _ in range(prev_count):
            prev = prev.next

        # print(prev.val)

        prev.next = prev.next.next  # disconnect that node 
    
        return head



# Optimal Using the Slow and Fast Pointer ( RATTA )
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(-1, head)  # dummy node is created to handle the case when we want to delete head
        fast = dummy 
        slow = dummy

        # we moved n+1 to maintain the GAP of N+1 in between the node.. so
        for _ in range(n+1):
            fast = fast.next 
        
        # because of N+1 gap .. now slow will end at the prev of the node which needs to be deleted   
        while fast:
            fast = fast.next 
            slow = slow.next 
        
        slow.next = slow.next.next 

        return dummy.next

