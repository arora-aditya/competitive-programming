# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        https://leetcode.com/problems/middle-of-the-linked-list/description/
        :type head: ListNode
        :rtype: ListNode
        """
        x1, x2 = head, head
        while x2 and x2.next:
            x1 = x1.next
            x2 = x2.next.next
            # print(x1.val, x2.val)
        return x1
