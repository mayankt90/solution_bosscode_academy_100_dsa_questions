############################################### Question #########################################################

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0] 
'''

############################################### Solution In Python ########################################################

# This solution uses two loops to calculate the product of all elements except the current one giving time complexity of O(n^2).

# Solution 1
def productExceptSelf(nums):
    l = []
    val = 1
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if i!=j:
                val = val*nums[j]
        l.append(val)
        val = 1
    return l

val = productExceptSelf([1,2,3,4])
print(val) # [24, 12, 8, 6]
val01 = productExceptSelf([-1,1,0,-3,3])    
print(val01) # [0, 0, 9, 0, 0] 

# Solutuion 2
# This solution uses a single loop to calculate the product of all elements except the current one giving time complexity of O(n).
def productExceptSelf(nums):
    total_product = 1
    zero_count = 0

    for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
    result = []
    for num in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            result.append(total_product if num == 0 else 0)
        else:
            result.append(total_product // num)
    return result

val = productExceptSelf([1, 2, 3, 4])
print(val)  # [24, 12, 8, 6]
val01 = productExceptSelf([-1, 1, 0, -3, 3])
print(val01)  # [0, 0, 9, 0, 0]


