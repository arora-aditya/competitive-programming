def totalHammingDistance(nums):
        """
        https://leetcode.com/problems/total-hamming-distance/description/
        :type nums: List[int]
        :rtype: int
        """
        def points_of_binary_difference(x,y):
            x_bin="{0:b}".format(x)
            y_bin="{0:b}".format(y)
            k=max(len(x_bin),len(y_bin))
            x_bin='0'*(k-len(x_bin))+x_bin
            y_bin='0'*(k-len(y_bin))+y_bin
            count=0
            for i in range(k):
                if x_bin[i] != y_bin[i]:
                    count += 1
            return count
        answer=0
        if len(nums) != 0:
            for i in range(0,len(nums)-1):
                for j in range(i,len(nums)):
                    answer += points_of_binary_difference(nums[i],nums[j])
        return answer

print(totalHammingDistance([4,14,2]))
