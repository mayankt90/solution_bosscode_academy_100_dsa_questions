############################################### Question #########################################################

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

############################################### Solution In Python ##################################################

#Solution 1: Brute Force TLE 111 / 126 testcases passed 

def groupAnagrams(strs):
    anagrams = {}
    for i in range(len(strs)):
        str_temp = ''.join(sorted(strs[i]))
        if str_temp not in anagrams:
            temp = [strs[i]]
            for j in range(i+1,len(strs)):
                cmp_str = ''.join(sorted(strs[j]))
                if str_temp == cmp_str:
                    temp.append(strs[j])
            anagrams[str_temp] = temp
    return list(anagrams.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))


#Solution 2: Optimized Code
def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())

# Example usage:
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))

        
        
        
