############################################### Question #########################################################

'''
iven an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
'''

############################################### Solution In Python ##################################################

#Solution 1
def sortColors(nums):
    nums.sort()
    return nums

sortColors([2,0,2,1,1,0])   
print(sortColors([2,0,2,1,1,0]))

#Solution 2

def sortColors(nums):
    zero = 0
    one = 0
    two = 0

    for i in nums:
        if i == 0:
            zero += 1
        elif i == 1:
            one += 1
        else:
            two += 1
    
    for i in range(zero):
        nums[i] = 0
    for i in range(zero, zero+one):
        nums[i] = 1
    for i in range(zero+one, zero+one+two):
        nums[i] = 2
    return nums

sortColors([2,0,2,1,1,0])
print(sortColors([2,0,2,1,1,0]))

    
