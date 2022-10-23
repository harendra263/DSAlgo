class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        lh = len(haystack)
        ln = len(needle)

        return next(
            (
                i
                for i in range(lh)
                if needle[0] == haystack[i]
                and i + ln <= lh
                and haystack[i : i + ln] == needle
            ),
            -1,
        )