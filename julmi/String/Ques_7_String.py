############################################### Question #########################################################

'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the 
number of times it appears in the string. Return the sorted string. If there are multiple answers, return any of them.


Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

############################################### Solution In Python ##################################################

#Solution 1: Brute Force 

def frequencySort(s):
    freq_dict = {}
    for c in s:
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1
    
    freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for c, freq in freq_dict:
        result += c * freq
    return result

print(frequencySort("tree"))
