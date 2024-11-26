# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# ITERATIVE : T O(n) / S O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            # Store next value to continue iteration after reversal
            temp = head.next
            # Link the head's next node to the previous one (reverse link)
            head.next = prev
            # set prev to current node
            prev = head\
            # set head to stored next node ( before breaking the link ) 
            head = temp
        
        # At the end of the loop prev equals the new head
        return prev



# RECURSIVE : T O(n) / S O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # edge case (empty listnode) + base case (next after tail is None)
        if not head or not head.next:
            return head

        # recursive call, only the last new_head value is used
        new_head = self.reverseList(head.next)
        # node to the right of head now points to head (reverse link)
        head.next.next = head
        # head points to None (will be changed unless its the final head)
        head.next = None

        # The last return is used and returns the head of the reversed linked list
        return new_head
