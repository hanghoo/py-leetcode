# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a, b = head, head
        for _ in range(k):
            if b is not None:
                b = b.next
            else:
                return head
        newHead = self.reverseN(a, k)
        a.next = self.reverseKGroup(b, k)
        return newHead

    
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # method 1
        pre, cur, nxt = None, head, head.next
        for _ in range(n):
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next
            # 反转后跟原链表后面的部分接上
            head.next = cur
        return pre

        # method 2
        # self.successor = None
        # if n == 1:
        #     self.successor = head.next
        #     return head

        # last = self.reverseN(head.next, n-1)
        # head.next.next = head
        # head.next = self.successor
        # return last
