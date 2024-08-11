class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        longest = start = 0
    
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            longest = max(longest, i - start + 1)
        return longest