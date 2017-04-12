# Author: Steven Wang    Date: 20170408
# 1 Two_Sum

nums = [1,2,3,4]

range(10)

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    return_list = []

    for i in range(len(nums)):
        for c in range(i+1, len(nums)):
            if nums[i] + nums[c] == target:
                return_list.append(i)
                return_list.append(c)
    
    return return_list
    
twoSum(nums, 5)




    

        