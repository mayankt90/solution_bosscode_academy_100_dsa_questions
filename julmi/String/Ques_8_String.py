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

Example 4:
Input: s = "())()(((" 
Output: "()()"
'''

############################################### Solution In Python ##################################################

#Solution 1: Brute Force 32 / 62 testcases passed

# pick the places which are incompatable with their location in the dict and remove them.

def minRemoveToMakeValid(s):
    dict_ = {}
    for i in range(len(s)):
        if s[i] == '(':
            dict_[i] = '('
        elif s[i] == ')':
            keys = list(dict_.keys())
            if keys: 
                last_key = keys[-1]
                if dict_[last_key] == '(':
                    dict_.pop(last_key)
                else:
                    dict_[i] = ')'
            else:
                dict_[i] = ')'
    
    indices_to_remove = list(dict_.keys())
    s_list = list(s)
    for index in indices_to_remove:
        s_list[index] = ''
    result = ''.join(s_list)
    return result

print(minRemoveToMakeValid("(t(e)y))d(()(e("))

# Solution 2:



def minRemoveToMakeValid(s):
    s_list = list(s)
    stack = []
                
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  
        elif char == ')':
            if stack:
                stack.pop()  
            else:
                s_list[i] = ''  

    for i in stack:
        s_list[i] = ''

    return ''.join(s_list)

print(minRemoveToMakeValid("(()))(()))"))



## Both Solution are identical test case are workinig on the local machine but not on the leetcode platform, may be due to the 
# leetcode platform not supporting the latest version of python or leetcode platform has a different approach to handle the 
# time limit exceeded error.

