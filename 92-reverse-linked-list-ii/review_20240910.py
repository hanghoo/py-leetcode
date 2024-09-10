# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # method 1
        # if head is None or head.next is None:
        #     return head
        # pre, cur, nxt = None, head, head.next
        # for _ in range(n):
        #     cur.next = pre
        #     pre = cur
        #     cur = nxt
        #     if nxt is not None:
        #         nxt = nxt.next
        #     # 反转后跟原链表后面的部分接上
        #     head.next = cur
        # return pre

        # method 2
        self.successor = None  # 因为要successor栈顶的值，所以需要self
        if n == 1:
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last
