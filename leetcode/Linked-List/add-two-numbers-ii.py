class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        st1 , st2= [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        prev = None
        carry = 0
        while st1 != [] and st2 != []:

            su = (st1.pop() + st2.pop() + carry)
            l = ListNode(su%10)
            carry = su//10
            l.next = prev
            prev = l
            # print(prev)
        while st1 != []:
            su = (st1.pop() + carry)
            l = ListNode(su%10)
            carry = su//10
            l.next = prev
            prev = l
        while st2 != []:
            su = (st2.pop() + carry)
            l = ListNode(su%10)
            carry = su//10
            l.next = prev
            prev = l
        if carry != 0:
            l = ListNode(carry)
            l.next = prev
        # l = ListNode(su%10)
        # l.next = prev
        return l
