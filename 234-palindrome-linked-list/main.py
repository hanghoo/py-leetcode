# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if head == None or head.next == None:
            return head
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
