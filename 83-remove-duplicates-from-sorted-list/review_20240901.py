# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        if fast is None:
            return head
        while fast:
            if fast.val != slow.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        slow.next = None
        return head
