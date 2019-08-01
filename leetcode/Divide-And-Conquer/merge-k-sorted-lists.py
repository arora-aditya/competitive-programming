# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # https://leetcode.com/problems/merge-k-sorted-lists/
        merged=[]
        for li in lists:
            while li:
                merged.append(li)
                li=li.next
        merged.sort(key=lambda x:x.val)
        for i in range(len(merged)-1):
            merged[i].next=merged[i+1]
        if merged==[]:
            return None
        else:
            return merged[0]