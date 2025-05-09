############################################### Question #########################################################

'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

############################################### Solution In Python ##################################################

#Solution 1 264/268 TLE in 4 test cases

def minWindow(s, t):
    s_length = len(s)
    t_length = len(t)
    result = []
    
    # Helper function to check character counts
    def has_sufficient_chars(sub, target):
        for char in set(target):
            if sub.count(char) < target.count(char):
                return False
        return True

    # Main logic
    for i in range(s_length - t_length + 1):
        for j in range(i + t_length - 1, s_length):
            sub_str = s[i:j+1]
            if has_sufficient_chars(sub_str, t):
                result.append(sub_str)
                break

    return min(result, key=len) if result else ""

# Test cases
print(minWindow("bbaa", "aba"))          # Should return "baa"
print(minWindow("a", "a"))               # Should return "a"
print(minWindow("ADOBECODEBANC", "ABC")) # Should return "BANC"

#Solution 2