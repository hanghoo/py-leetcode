class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # 由于单链表的结构，至少要用三个指针才能完成迭代反转
        # cur 是当前遍历的节点，pre 是 cur 的前驱结点，nxt 是 cur 的后继结点
        pre, cur, nxt = None, head, head.next
        while cur:
            # 逐个结点反转
            cur.next = pre
            # 更新指针位置
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        return pre
