# https://youtu.be/ZW7st_pN05w
class Solution:
    def reverseBits(self, n):
        res = 0

        for _ in range(32):
            mask = n & 1
            n = n >> 1
            res = res << 1
            res = res | mask

        return res