############################################### Question #########################################################

'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses
 string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''

############################################### Solution In Python ##################################################

#Solution 1: Brute Force 14/50 Test cases passed

def minRemoveToMakeValid(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                s = s[:i] + s[i+1:]
                stack.append(i)
    print(stack)
    
    # for i in range(len(stack)):
    #     j = 0
    #     while j < len(s):
    #         if stack[i] == s[j]:
    #             s = s[:j] + s[j+1:]
    #             break
    #         j += 1
    # return s
    

print(minRemoveToMakeValid("())()((("))


