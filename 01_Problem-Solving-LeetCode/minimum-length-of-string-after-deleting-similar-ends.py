# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, len(s)-1
        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and c == c:
                left += 1
            while left <= right and s[right] == c:
                right -= 1
        return right-left+1
