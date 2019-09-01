# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # https://leetcode.com/problems/reorder-list/
        st = []
        traverser = head
        while traverser:
            st.append(traverser)
            traverser = traverser.next
        # print([x.val for x in st])
        traverser = head
        if len(st) > 0:
            last = st.pop()
        else:
            return
        le = len(st)
        counter = 0
        while counter < le:
            # print(traverser.val)
            first = traverser
            second = traverser.next
            first.next = last
            last.next = second
            last = st.pop()
            traverser = second
            counter += 2
        # print('HERE')
        # print(traverser.val)
        traverser.next = None
            