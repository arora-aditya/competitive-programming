class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # https://leetcode.com/problems/missing-ranges/
        if not nums:
            if lower != upper:
                return [str(lower) + "->" + str(upper)]
            return [str(lower)]
        if lower == upper == nums[0]:
            return []
        ranges = []
        k = -1
        if lower != nums[0]:
            ranges.append([lower, nums[0]-1])
            k = 0
        else:
            for i in range(1, len(nums)):
                print(i, 'here')
                if nums[i] != nums[i-1] + 1 and nums[i] != nums[i-1]:
                    ranges.append([nums[i-1]+1, nums[i]-1])
                    k = i
                    break
        print(ranges)
        if k != -1:
            for i in range(k+1, len(nums)):
                if nums[i] != nums[i-1] + 1 and nums[i] != nums[i-1]:
                    print(i, 'here')
                    # if nums[i] != ranges[-1][1] + 1:
                    #     ranges[-1][1] = nums[i] - 1
                    # else:
                    ranges.append([nums[i-1]+1, nums[i]-1])
        print(ranges)
        if nums[-1] != upper:
            ranges.append([nums[-1]+1, upper])
        print(ranges)
        for i in range(len(ranges)):
            if ranges[i][0] == ranges[i][1]:
                ranges[i] = str(ranges[i][0])
            else:
                ranges[i] = str(ranges[i][0]) + "->" + str(ranges[i][1])
        return ranges
