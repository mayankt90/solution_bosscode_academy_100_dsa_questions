############################################## Question ##########################################################

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

############################################### Solution In Python ##################################################

#Solution 1: Brute Force 

def backtrack(result, n, s='', left=0, right=0):
    if len(s) == 2*n:
        result.append(s)
        return
    if left < n:
        backtrack(result, n, s+'(', left+1, right)
    if right < left:
        backtrack(result, n, s+')', left, right+1)
        
def generateParenthesis(n):
    result = []
    backtrack(result, n , '', 0, 0)
    return result

print(generateParenthesis(3))
print(generateParenthesis(1))
    