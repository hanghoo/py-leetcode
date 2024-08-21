# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        x = self.findFromEnd(dummy, n+1)
        x.next = x.next.next
        return dummy.next

    def findFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = head
        for _ in range(k):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
