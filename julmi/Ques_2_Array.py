############################################### Question #########################################################

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

############################################### Solution In Python ########################################################

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    insert_pos = 0
    zero_count = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[insert_pos] = nums[i]
            insert_pos+=1
        else:
            zero_count+=1
    for i in range(zero_count):
        nums[insert_pos] = 0
        insert_pos+=1
    return nums

print(moveZeroes([0,1,0,3,12])) # [1, 3, 12, 0, 0]
print(moveZeroes([0])) # [0]
print(moveZeroes([0,0,0,0])) # [0, 0, 0, 0]
        
