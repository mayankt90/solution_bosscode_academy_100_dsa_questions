############################################### Question #########################################################

'''
Given an array of positive integers nums and a positive integer target, return 
the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, 
return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
'''

############################################### Solution In Python ##################################################

#Solution 1

# def minSubArrayLen(target, nums):
#     l = []
#     for i in range(len(nums)):
#         sum_var = 0
#         count_var = 0
#         for j in range(i, len(nums)):
#             sum_var += nums[j]
#             count_var += 1
#             if sum_var >= target:
#                 l.append(count_var)
#             if sum_var > target:
#                 break
#     print(l)
#     if len(l) == 0:
#         return 0
#     return min(l)
            
# print(minSubArrayLen(7, [2,3,1,2,4,3])) 
# print(minSubArrayLen(4, [1,4,4])) 
# print(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) 
# print(minSubArrayLen(11, [1,2,3,4,5]))

#Solution 2

def minSubArrayLen(target, nums):
    left = 0
    right = 0
    current_sum = 0
    min_length = float('inf')
    
    while right < len(nums):
        current_sum += nums[right]
        right +=1

        while current_sum >= target:
            min_length = min(min_length,right-left)
            current_sum-= nums[left]
            left +=1
    return min_length if min_length != float('inf') else 0

print(minSubArrayLen(7, [2,3,1,2,4,3])) 
print(minSubArrayLen(4, [1,4,4])) 
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) 
print(minSubArrayLen(11, [1,2,3,4,5]))

            




