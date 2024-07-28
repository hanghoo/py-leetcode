# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur, nxt = None, a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        a = b = head
        for i in range(k):
            if b == None:
                return head
            b = b.next
        # 翻转[a,b)
        newhead = self.reverse(a,b)
        a.next = self.reverseKGroup(b,k)
        return newhead
