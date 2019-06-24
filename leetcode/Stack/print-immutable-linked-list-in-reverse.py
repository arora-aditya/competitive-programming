# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
        st = []
        node = head
        while node:
            st.append(node)
            node = node.getNext()
        while st:
            st.pop().printValue()
        