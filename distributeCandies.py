import operator
def distributeCandies(candies):
    """
    https://leetcode.com/problems/distribute-candies/#/description
    :type candies: List[int]
    :rtype: int
    """
    candies.sort()
    total_unique=len(set(candies))
    total_count=len(candies)
    if total_unique * 2 <= total_count:
        return total_unique
    else:
        return int(total_count/2)

lel=(distributeCandies([0,1,2,3]))
print(lel)
