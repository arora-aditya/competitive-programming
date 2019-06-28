# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = pa = ListNode(-1)
        mod = 0
        while l1 != None and l2 != None:
            suu = l1.val + l2.val + mod
            su, mod = suu%10, suu//10
            re.next = ListNode(su)
            re = re.next
            l1 = l1.next
            l2 = l2.next
        # print(mod, l1.val)
        while l1 != None:
            suu = l1.val + mod
            su, mod = suu%10, suu//10
            re.next = ListNode(su)
            re = re.next
            l1 = l1.next
        while l2!= None:
            suu = l2.val + mod
            su, mod = suu%10, suu//10
            re.next = ListNode(su)
            re = re.next
            l2 = l2.next
        if mod != 0:
            re.next = ListNode(mod)
            re = re.next
        return pa.next