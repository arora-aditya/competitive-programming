# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        https://leetcode.com/problems/merge-k-sorted-lists/description/
        """
        r = ListNode(0.12345)
        s = r
        le = len(lists)
        while le != 0:
            if le == 1 and lists[0] is None:
                return lists[0]
            mi, le = self.findSmallest(lists, le)
            if mi == float('Inf'):
                return None
            # print("min2", mi)
            s.next = ListNode(mi)
            s = s.next
        return r.next

    def findSmallest(self, lists, le):
        j = -1
        mi = float('Inf')
        i = 0
        while i < le:
            # print("min0", mi)
            # print("vals", lists[i].val)
            if lists[i] is None:
                lists.pop(i)
                le -= 1
                continue
            if mi > lists[i].val:
                mi = lists[i].val
                j = i
            i += 1
        # print("min1", mi)
        if j != -1:
            lists[j] = lists[j].next
            if lists[j] is None:
                lists.pop(j)
                le -= 1
        return mi, le
