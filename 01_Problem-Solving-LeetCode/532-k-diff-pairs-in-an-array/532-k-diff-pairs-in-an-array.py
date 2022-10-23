class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        countDict = {}
        for i in nums:
            if i not in countDict: countDict[i] = 1
            else: countDict[i] += 1

        return sum(
            k == 0 and value > 1 or k != 0 and k + i in countDict
            for i, value in countDict.items()
        )