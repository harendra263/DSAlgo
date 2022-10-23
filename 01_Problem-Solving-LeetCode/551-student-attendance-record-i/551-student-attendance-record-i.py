class Solution:
    def checkRecord(self, s: str) -> bool:
        count = {'A': 0}
        L = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count['A'] += 1        
                L = 0
            elif s[i] == 'L':
                if i > 0 and s[i-1] == 'L':
                    L += 1
                else:
                    L = 1
                if L >= 3: return False
            else:
                L = 0

        return count['A'] < 2