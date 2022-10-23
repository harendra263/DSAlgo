class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(s) + 1) for _ in range(len(p) + 1)]

        for i in range(len(dp)-1, -1, -1):
            for j in range(len(dp[0])-1, -1, -1):
                if i == len(dp)-1 and j == len(dp[0])-1:
                    dp[i][j] = True
                elif i == len(dp)-1:
                    dp[i][j] = False
                elif j == len(dp[0])-1:
                    dp[i][j] = dp[i+1][j] if p[i] == '*' else False
                elif p[i] == "?" or p[i] != '*' and p[i] == s[j]:
                    dp[i][j] = dp[i+1][j+1]
                elif p[i] == '*':
                    dp[i][j] = dp[i+1][j] or dp[i][j+1]
                else:
                    dp[i][j] = False

        return dp[0][0]