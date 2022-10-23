# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif not stack or lookup[stack.pop()] != parenthese:
                return False
        return not stack

