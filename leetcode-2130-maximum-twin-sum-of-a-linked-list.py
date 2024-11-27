# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = reverseListNode(slow)

        ans = 0
        while slow:
            ans = max(slow.val + head.val, ans)
            head = head.next
            slow = slow.next

        return ans

def reverseListNode(head):
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev
