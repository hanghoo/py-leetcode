# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)  # 加上dummy防止empty
        p3 = self.findFromEnd(dummy, n+1) # 倒数第几个的话，前面加一个dummy不影响
        p3.next = p3.next.next
        return dummy.next

    def findFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2
