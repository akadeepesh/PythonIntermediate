"""You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.


Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        pos = 0
        max_word = ""
        if(len(word1) > len(word2)):
            max_word = word1
        elif(len(word1) < len(word2)):
            max_word = word2
        while pos < min(len(word1), len(word2)):
            word += word1[pos] + word2[pos]
            pos += 1
            if(pos == min(len(word1), len(word2))):
                word += max_word[pos: ]
                break
        return word
    
word1 = "abcd"
word2 = "pqrs"
sol = Solution()
print(sol.mergeAlternately(word1, word2))
    
