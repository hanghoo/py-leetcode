# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #递归出口
        if(left == 1):
            rev_head = self.reverseN(head, right)
            return rev_head
            #return self.reverseN(head, right)
        #递归
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    # self.successor ensures that the successor node is shared across recursive calls 
    # and persists beyond a single function call
    # 反转链表前N个节点，返回反转后的头结点
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(n == 1):
            self.successor = head.next
            return head

        rev_head = self.reverseN(head.next, n-1)

        head.next.next = head
        head.next = self.successor
        return rev_head

