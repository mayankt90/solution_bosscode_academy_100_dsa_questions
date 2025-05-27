############################################### Question #########################################################

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.
'''

############################################### Solution In Python ##################################################

#Solution 1: Brute Force 25/49 Test cases 50 %

def characterReplacement(s, k):
    s = s[::-1]
    print(s)
    max_lenght = 0

    for i in range(len(s)):
        valk = k
        count = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count += 1
            else:
                if valk > 0:
                    valk -= 1
                    count += 1
                else:
                    break
            max_lenght = max(max_lenght, count)
    return max_lenght

#Solution 2: Sliding Window

                

                



print(characterReplacement("ABAB", 2))
