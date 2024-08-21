class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0)  # dummy head node
        self.tail = self.dummy
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        return current.val


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1

        new_node = ListNode(val)

        if index == self.size:
            self.tail.next = new_node
            self.tail = new_node

        current = self.dummy
        for _ in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        if index == self.size - 1:  # 如果删除last node需要更新self.tail
            self.tail = current
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
