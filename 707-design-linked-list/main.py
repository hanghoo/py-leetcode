class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None  # head是一个节点
        self.size = 0


    def get(self, index: int) -> int:
        # index invalid
        if index < 0 or index >= self.size:
            return -1

        current_node = self.head  # current_node也是节点

        for _ in range(index):
            current_node = current_node.next
        return current_node.val


    def addAtHead(self, val: int) -> None:
        # LinkedList empty
        if self.size = 0:
            self.head = ListNode(val)
        else:
            new_node = LinkedList(val)
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1


    def addAtTail(self, val: int) -> None:


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:  # checkPositionIndex
            return -1
        
         if (index == self.size) {
            addAtTail(val);
            return;
        }

        dummy = ListNode(0, self.head)
        current = dummy
        for i in range(index):  # 找到index Node的前一个
            current = current.next
        
        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
