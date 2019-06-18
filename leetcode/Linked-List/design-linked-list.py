class MyLinkedList:
    # https://leetcode.com/problems/design-linked-list/
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = []

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if len(self.li) > index and index >= 0:
            return self.li[index]
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.li = [val] + self.li
        # print(self.li)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.li.append(val)
        # print(self.li)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > len(self.li):
            return
        if index < 0:
            self.li = [val] + self.li
            return
        self.li = self.li[:index] + [val] + self.li[index:]
        # print(self.li)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # print(index, self.li)
        if index < len(self.li) and index >= 0:
            del self.li[index]
        # print(self.li)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)