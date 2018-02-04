class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        https://leetcode.com/problems/intersection-of-two-linked-lists/description/
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        di = collections.OrderedDict()
        while headA:
            di[headA] = 1
            headA = headA.next
        while headB:
            if headB in di:
                return headB
            else:
                di[headB] = 1
                headB = headB.next
        return None
