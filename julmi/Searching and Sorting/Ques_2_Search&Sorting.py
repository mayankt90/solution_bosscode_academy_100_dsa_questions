############################################## Question ##########################################################

'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.Note that it is the kth smallest element in the sorted order,
not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
'''

############################################### Solution In Python ##################################################

#Solution 1: Brute Force 

def kthSmallest(matrix, k):
    arr = []
    i_table = len(matrix)
    j_table = len(matrix[0])
    for i in range(i_table):
        for j in range(j_table):
            arr.append(matrix[i][j])
    arr.sort()
    return arr[k-1]

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(kthSmallest([[-5]], 1))


    


            