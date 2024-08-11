class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join(f'^{s}$')
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        start = (center_index - max_len) // 2

        return s[start:start + max_len]