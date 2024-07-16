# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        #print(f"this ListNode object is {id(dummy1)}")
        #print(f"this ListNode object is {id(dummy2)}")
        p1 = dummy1
        p2 = dummy2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            # 断开连接，并移到下一个节点
            tmp = p.next
            p.next = None
            p = tmp
        p1.next = dummy2.next
        return dummy1.next
