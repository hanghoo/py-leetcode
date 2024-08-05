# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    left = None
    res = True
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        self.traverse(head)
        return self.res
    
    def traverse(self, right: Optional[ListNode]):
        if right is None:
            return
        
        self.traverse(right.next)

        if self.left.val != right.val:
            self.res = False
        self.left = self.left.next
