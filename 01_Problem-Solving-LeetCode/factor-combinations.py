# Time:  O(nlogn)
# Space: O(logn)

class Solution(object):
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        result = []
        factors = []
        self.getResult(n, result, factors)
        return result

    def getResult(self, n, result, factors):
        i = factors[-1] if factors else 2
        while i <= n / i:
            if n % i == 0:
                factors.append(i)
                factors.append(n / i)
                result.append(list(factors))
                factors.pop()
                self.getResult(n / i, result, factors)
                factors.pop()
            i += 1

