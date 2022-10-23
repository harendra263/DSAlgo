class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        Sum = 0
        for num in nums:
            Sum += num
            runningSum.append(Sum)
        return runningSum
            