class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            a = str(n)
            n = sum(int(i)**2 for i in a)
            if n == 1: return True
            if n in visited: return False
            visited.add(n)

        return True