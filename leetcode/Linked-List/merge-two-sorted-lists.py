# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # https://leetcode.com/problems/merge-two-sorted-lists/description/
        head = ListNode(None)
        l = head
        l1Parse = l1
        l2Parse = l2
        while l1Parse is not None and l2Parse is not None:
            if l1Parse.val > l2Parse.val:
                l.val = l2Parse.val
                l2Parse = l2Parse.next
            else:
                l.val = l1Parse.val
                l1Parse = l1Parse.next
            add = ListNode(None)
            l.next = add
            l = l.next
        while l1Parse is not None:
            l.val = l1Parse.val
            add = ListNode(None)
            l.next = add
            l = l.next 
            l1Parse = l1Parse.next
        while l2Parse is not None:
            l.val = l2Parse.val
            add = ListNode(None)
            l.next = add
            l = l.next 
            l2Parse = l2Parse.next
        l = head
        while l.next is not None:
            if l.next.val is None:
                l.next = None
                break
            l = l.next
        if head.val is None:
            head = None
        return head