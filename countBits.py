def countBits(num):
    """
    https://leetcode.com/problems/counting-bits/#/description
    :type num: int
    :rtype: List[int]
    """
    def points_of_binary_difference(x,y):
        count=0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
        return count
    return_list=[]
    for i in range(num+1):
        x="{0:b}".format(i)
        return_list.append(points_of_binary_difference(x,len(x) * '0'))
    return return_list

print(countBits(5))
