# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 返回链表的倒数第 k 个节点
def findFromEnd(head: ListNode, k: int) -> ListNode:
    p1 = head
    # p1 先走 k 步
    for i in range(k):
        p1 = p1.next
    p2 = head
    # p1 和 p2 同时走 n - k 步
    while p1 != None:
        p2 = p2.next
        p1 = p1.next
    # p2 现在指向第 n - k + 1 个节点，即倒数第 k 个节点
    return p2

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 需要找到 倒数第 k+1 个节点，即第 n-k+2 个节点
        # 为了避免找 倒数第 k+1 个节点 出界，采用dummy
        dummy = ListNode(-1, head)
        p2 = findFromEnd(dummy, n+1)
        tmp = p2.next
        p2.next = p2.next.next
        tmp = None
        return dummy.next
