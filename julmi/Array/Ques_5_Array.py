############################################### Question #########################################################

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

############################################### Solution In Python ##################################################

#Solution 1:

def twoSum1(nums, target):
    target_list = []
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]:
            target_list.append(i)
            index = nums[i+1:].index(target - nums[i]) + (i + 1)
            target_list.append(index)
            break
    return target_list

#Solution 2: Hash Table Approach

def twoSum2(nums, target):
    # Create a dictionary to store the complement of each number
    num_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # If the complement exists in the dictionary, we found our pair
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Store the current number and its index in the dictionary
        num_dict[num] = i
    
    # Return empty list if no solution is found (though the problem guarantees one solution exists)
    return []

print("Solution 1 (Original Approach)")
print(twoSum1([2,7,11,15], 9)) # Output: [0,1]
print(twoSum1([3,2,4], 6)) # Output: [1,2]
print(twoSum1([3,3], 6)) # Output: [0,1]

print("\nSolution 2 (Hash Table Approach)")
print(twoSum2([2,7,11,15], 9)) # Output: [0,1]
print(twoSum2([3,2,4], 6)) # Output: [1,2]
print(twoSum2([3,3], 6)) # Output: [0,1]
