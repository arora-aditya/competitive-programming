# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    https://leetcode.com/problems/add-two-numbers/#/description
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    i = 1
    num = 0
    while l1.next != None and l2.next!= None:
        num += (l1.val + l2.val) * i
        i *= 10
        l1, l2 = l1.next, l2.next
    while l1.next != None:
        num += l1.val * i
        i *= 10
        l1 = l1.next   
    while l2.next != None:
        num += l2.val * i
        i *= 10
        l2 = l2.next
    print(num)
    l = ListNode(num%10)
    x = l
    num = num/10
    while num != 0:
        l_next = ListNode(num%10)
        l.next = l_next
        l_next = l
        num = num/10
    return x

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

l = (addTwoNumbers(l1,l2))
