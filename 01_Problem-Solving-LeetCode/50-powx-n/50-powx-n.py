class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        p = n
        if p < 0: p *= -1
        while p > 0:
            if p % 2 == 0:
                x *= x
                p /= 2
            else:
                res *= x
                p -= 1

        return 1 / res if n < 0 else res