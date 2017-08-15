def twoSumII(numbers,target):
    num_dict={}
    for i in range(len(numbers)):
        if numbers[i] in num_dict.keys():
            if target == 2 * numbers[i]:
                if num_dict[target-numbers[i]]>0:
                    return [numbers.index(target-numbers[i]),i]
                else:
                    num_dict[target-numbers[i]] += 1
            else:
                return [numbers.index(target-numbers[i]),i]
        else:
            num_dict[target-numbers[i]]=1



