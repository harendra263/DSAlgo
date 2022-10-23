class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[2**31]*n for _ in range(n)]
        for u, v, w in edges:
            dp[u][v] = w
            dp[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = 0 if i == j else min(dp[i][j], dp[i][k] + dp[k][j])
        res = 0
        min_reach = n
        for i in range(n):
            i_reach = sum(dp[i][j] <= distanceThreshold for j in range(n))
            print(i_reach)
            if i_reach <= min_reach:
                res = i
                min_reach = i_reach

        return res