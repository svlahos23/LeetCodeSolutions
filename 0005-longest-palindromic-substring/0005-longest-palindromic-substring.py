class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
    
    # Create a DP table to store the palindromic status
        dp = [[False] * n for _ in range(n)]
    
        start = 0
        max_length = 1
    
    # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
    
    # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
    
    # Check for palindromes of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the current substring
            
            # Check if the current substring is a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
    
    # Return the longest palindromic substring
        return s[start:start + max_length]