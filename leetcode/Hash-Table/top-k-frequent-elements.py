import operator
def topKFrequent(nums, k):
    """
    https://leetcode.com/problems/top-k-frequent-elements/#/description
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    num_dict={}
    for i in sorted(set(nums)):
        num_dict[i]=nums.count(i)
    num_dict = dict(sorted(num_dict.items(), key=operator.itemgetter(1),reverse=True))
    count=1
    return_list=[]
    for num in num_dict:
        if count <= k:
            count += 1
        else:
            break
        return_list.append(num)
    return return_list
