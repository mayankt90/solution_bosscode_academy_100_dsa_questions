############################################### Question #########################################################

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
 (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 
'''

############################################### Solution In Python ##################################################

#Solution 1:
#Approach:
#1. Brute Force in O(n^2)
#Code:
def maxArea_brute_force(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            if j-i > 0:
                area = min(height[i], height[j]) * (j-i)
                max_area = max(max_area, area)
    return max_area
    
max_area = maxArea_brute_force([1,8,6,2,5,4,8,3,7])
print(max_area) # Output: 49
max_area = maxArea_brute_force([1,1])
print(max_area) # Output: 1

#Solution 2:
#Approach:
#1. Two pointer approach in O(n)
#Code:
def maxArea_two_pointer(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate area with current pointers
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        max_area = max(max_area, area)
        
        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
    
max_area = maxArea_two_pointer([1,8,6,2,5,4,8,3,7])
print(max_area) # Output: 49
max_area = maxArea_two_pointer([1,1])
print(max_area) # Output: 1