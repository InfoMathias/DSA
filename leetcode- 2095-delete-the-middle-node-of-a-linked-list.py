# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If there's only one node, return None
        if head.next is None:
            return None
        
        link = None
        slow = head
        fast = head
        
        # Finding the middle node using slow and fast pointers
        while fast and fast.next:
            link = slow
            slow = slow.next
            fast = fast.next.next
        
        # Deleting the middle node by updating the link
        link.next = slow.next
        
        return head
