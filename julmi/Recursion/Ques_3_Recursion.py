############################################## Question ##########################################################

'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''

############################################### Solution In Python ##################################################

#Solution 1: Backtracking

"""
Level0: []
level1: [1]                  [2]              [3]
level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          

"""

def permute(nums):
    visited = []
    res = []
    backtracking(res, visited, [], nums)
    return res

def backtracking(res, visited, subset, nums):
    if len(subset) == len(nums):
        res.append(subset)
        return
    for i in range(len(nums)):
        if i not in visited:
            visited.append(i)
            backtracking(res, visited, subset + [nums[i]], nums) # Here subset + [nums[i]] is creating a new list.
            visited.remove(i)  
            
print(permute([1,1,3]))




