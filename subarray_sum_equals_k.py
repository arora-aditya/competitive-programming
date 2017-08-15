def subarray_sum(nums,k):
    count=0
    for i in range(len(nums)):
        j=i
        save=0
        while save != k and j < len(nums):
            save=save+nums[j]
            j += 1
        if save == k and k!=0:
            count += 1
    return count

nums=[1]
print(subarray_sum(nums,0))
