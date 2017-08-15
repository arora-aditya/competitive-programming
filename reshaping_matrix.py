def reshaping_matrix(nums,r,c):
    new_matrix=[]
    list_of_numbers=[]
    count=0
    if r*c==len(nums)*len(nums[0]):
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                list_of_numbers.append(nums[i][j])
        print(list_of_numbers)
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(list_of_numbers[count])
                count+=1
            new_matrix.append(row)
        print(new_matrix)
    else:
        print(nums)

nums=[[1,2,3],[4,5,6]]
reshaping_matrix(nums,3,2)
