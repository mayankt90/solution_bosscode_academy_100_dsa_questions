############################################### Question #########################################################

'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
'''

############################################### Solution In Python ##################################################

# Understand what is lexicographical order and how to find the next permutation.

#Solution 1:

#Approach:

# If array is sorted in descending order, then it is the last permutation then return reverse of the array. Otherwise:
# 1.  Pivot: Find the first index i such that nums[i] < nums[i + 1]. If no such index exists, the permutation is the last permutation.
# 2. Find the number from right side which is the successor of nums[i] and swap it with nums[i].
# 3. Arrange the number after i in ascending order.
# 4. Return the nums.

#Code:

def nextPermutation(nums):
    if nums == sorted(nums, reverse=True):
        nums.reverse()
        return nums
    
    n = len(nums)
    i = n - 1
    
    while i > 0:
        if nums[i - 1] < nums[i]:
            break
        i -= 1
    j = i  

    val = float('inf')
    index = i - 1

    while j < n:
        if nums[j] > nums[i - 1]:
            if nums[j] < val:
                val = nums[j]
                index = j
        j += 1

    nums[i - 1], nums[index] = nums[index], nums[i - 1]
    nums[i:] = sorted(nums[i:])
    return nums






#Solution Did't work as expected. 
# def nextPermutation(nums):
#     n = len(nums)
#     i = n - 1
#     last = n - 1
#     flag = 0
#     while i > 0:
#         if nums[i - 1] <= nums[i]:
#             nums[i - 1], nums[i] = nums[i], nums[i - 1]
#             flag = 1
#             break
#         else:
#             nums[i - 1], nums[i] = nums[i], nums[i - 1]
#         i -= 1
#     if flag == 0:
#         nums.reverse()
#     return nums

next_permutation = nextPermutation([1,3,2])
print(next_permutation)  # Output: [2, 1, 3]
next_permutation = nextPermutation([1, 2, 3])
print(next_permutation)  # Output: [1, 3, 2]
next_permutation = nextPermutation([3, 2, 1])
print(next_permutation)  # Output: [1, 2, 3]
next_permutation = nextPermutation([2, 3, 1])
print(next_permutation)  # Output: [3, 1, 2]


   



