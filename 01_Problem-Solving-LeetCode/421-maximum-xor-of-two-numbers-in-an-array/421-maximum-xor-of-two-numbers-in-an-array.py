class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNum = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, num):
        cur = self.root
        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0
            if bit not in cur.children:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
        cur.endNum = num
        
    def findMaximumXOR(self, nums):
        for num in nums:
            self.add(num)
        res = 0
        tmp = 0
        for num in nums:
            cur = self.root
            for i in range(31, -1, -1):
                bit  = 0 if num & (1 << i) else 1
                if (
                    bit == 0
                    and 0 in cur.children
                    or bit != 0
                    and 1 not in cur.children
                ): cur = cur.children[0]
                else: cur = cur.children[1]
            res = max(res, num ^ cur.endNum)

        return res