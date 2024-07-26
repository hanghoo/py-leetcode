# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head,right)
        
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    
    # 反转以 head 为起点的 n 个节点，返回新的头结点
    def reverseN(self, head, n):
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n - 1)

        head.next.next = head
        head.next = self.successor
        return last
