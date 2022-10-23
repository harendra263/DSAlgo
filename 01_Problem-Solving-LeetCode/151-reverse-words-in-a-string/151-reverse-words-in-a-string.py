class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        j = i
        n = len(s)
        res = ""
        while i < n:
            if s[i] == " ":
                i += 1
            else:
                j = i
                while j < n and s[j] != " ":
                    j += 1
                subStr = s[i:j]
                res = subStr if res == "" else f"{subStr} {res}"
                i = j

        return res
            