class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini = 2**31

        for i in range(1, len(arr)):
            mini = min(mini, arr[i] - arr[i-1])

        return [
            [arr[i - 1], arr[i]]
            for i in range(1, len(arr))
            if arr[i] - arr[i - 1] == mini
        ]