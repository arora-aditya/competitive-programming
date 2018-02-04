class Solution(object):
    def reverseList(self, head):
        """
        https://leetcode.com/problems/reverse-linked-list/description/
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        li = []
        while head:
            li.append(head.val)
            head = head.next
        li = li[::-1]
        head = ListNode(li[0])
        sa = head
        for i in li[1:]:
            ne = ListNode(i)
            head.next = ne
            head = head.next
        return sa
