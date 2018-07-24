# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        x1, x2 = newHead, newHead

        for i in range(n):
            x2 = x2.next

        while x2 and x2.next:
            x2 = x2.next
            x1 = x1.next

        x1.next = x1.next.next

        return newHead.next
