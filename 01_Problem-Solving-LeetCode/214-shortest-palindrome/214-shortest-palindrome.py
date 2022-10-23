class Solution:
    def shortestPalindrome(self, s: str) -> str:
        m = next(
            (
                i
                for i in range(len(s) - 1, -1, -1)
                if s[: i + 1] == s[: i + 1][::-1]
            ),
            len(s) - 1,
        )

        return s[m+1:][::-1] + s