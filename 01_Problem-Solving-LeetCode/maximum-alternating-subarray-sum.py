# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maximumAlternatingSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kadane(nums, start):
            result = float("-inf")
            curr = odd = 0
            for i in xrange(start, len(nums)):
                curr = max(curr-nums[i], 0) if odd else curr+nums[i]
                result = max(result, curr)
                odd ^= 1
            return result

        return max(kadane(nums, 0), kadane(nums, 1))
