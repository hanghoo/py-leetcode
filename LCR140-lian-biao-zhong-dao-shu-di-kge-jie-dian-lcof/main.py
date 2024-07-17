# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        p1 = head
        for i in range(cnt):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
