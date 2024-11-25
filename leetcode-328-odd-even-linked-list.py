# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        even_head, odd_head, even_tail, odd_tail = None, None, None, None

        i = 1
        while head:
            if i % 2 == 0:
                if not even_tail:
                    even_tail = head
                    even_head = even_tail
                else:
                    even_tail.next = head
                    even_tail = even_tail.next
            else:
                if not odd_tail:
                    odd_tail = head
                    odd_head = odd_tail
                else:
                    odd_tail.next = head
                    odd_tail = odd_tail.next

            head = head.next
            i += 1
        
        odd_tail.next = even_head
        even_tail.next = None

        return odd_head
        
