def subarray_sum(nums,k):
    sums = {0:1} # prefix sum array
    res = s = 0
    for n in nums:
        s += n # increment current sum
        res += sums.get(s - k, 0) # check if there is a prefix subarray we can take out to reach k
        sums[s] = sums.get(s, 0) + 1 # add current sum to sum count
    return res
nums=[1]
print(subarray_sum(nums,6))
                
