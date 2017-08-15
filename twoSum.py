def twoSum(nums,target):
    num_dict={}
    for i in range(len(nums)):
        if nums[i] in num_dict.keys():
            if target == 2 * nums[i]:
                if num_dict[target-nums[i]]>0:
                    return [nums.index(target-nums[i])+1,i+1]
                else:
                    num_dict[target-nums[i]] += 1
            else:
                return [nums.index(target-nums[i])+1,i+1]
        else:
            num_dict[target-nums[i]]=1
                
print(twoSum([-1,0],-1))
