############################################### Question #########################################################

'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

############################################### Solution In Python ##################################################

#Solution 1

def findAnagrams(s, p):
    result = []
    s_lenght = len(s)
    p_lenght = len(p)
    if s_lenght < p_lenght:
        return result
    p1 = 0
    p2 = p_lenght - 1

    while p2 < s_lenght:
        sub_str = s[p1:p2+1]
        if sorted(sub_str) == sorted(p):
            result.append(p1)
        p1 += 1
        p2 += 1
        
    return result       
        
        
print(findAnagrams("cbaebabacd", "abc")) 
print(findAnagrams("abab", "ab"))

#Solution 3 - Using list of substrings

def findAnagrams(s, p):
    result = []
    s_length = len(s)
    p_length = len(p)
    
    if s_length < p_length:
        return result
    # Sort the pattern once
    sorted_p = sorted(p)
    # Create a list to store all substrings of length p
    substrings = []
    # Collect all substrings
    for i in range(s_length - p_length + 1):
        substrings.append(s[i:i + p_length])
    # Compare each substring with the sorted pattern
    for i, sub_str in enumerate(substrings):
        if sorted(sub_str) == sorted_p:
            result.append(i)

    return result

print(findAnagrams("cbaebabacd", "abc")) 
print(findAnagrams("abab", "ab"))

    
    
