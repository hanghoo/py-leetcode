# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        # 区间
        a, b = head, head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        newHead = self.reverseN(a, k)
        a.next = self.reverseKGroup(b, k)
        return newHead

    # 反转链表前N个节点，返回反转后的头结点
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 用迭代的方法
        pre = None
        cur = head
        nxt = head
        # while 终止的条件改一下就行了
        for _ in range(n):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # 返回反转后的头结点
        head.next = cur
        return pre
