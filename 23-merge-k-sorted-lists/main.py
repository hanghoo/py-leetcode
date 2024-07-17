# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(-1)
        p = dummy
        pq = []
        for head in lists:
            if head:  # 链表非空
                heapq.heappush(pq, (head.val, id(head), head))
                # id() used for TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
                #heapq.heappush(pq, (head.val, head))
        while pq:
            node = heapq.heappop(pq)[2]
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next), node.next))
                #heapq.heappush(pq, (node.next.val, node.next))
            p = p.next
        return dummy.next
