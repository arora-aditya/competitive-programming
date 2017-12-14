# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        https://leetcode.com/problems/palindrome-linked-list/description/
        :type head: ListNode
        :rtype: bool
        """
        st = []
        while head != None:
            st.append(head.val)
            head = head.next
            # print(st)
        return st == st[::-1]
