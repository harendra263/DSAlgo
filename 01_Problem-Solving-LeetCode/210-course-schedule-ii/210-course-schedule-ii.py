class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for a in prerequisites:
            adjList[a[0]].append(a[1])

        outbound = {i:0 for i in range(numCourses)}
        for a in prerequisites:
            outbound[a[1]] += 1

        q = [i for i, value in outbound.items() if value == 0]
        res = []

        while q:
            a = q.pop()
            res.append(a)
            for i in adjList[a]:
                outbound[i] -= 1
                if outbound[i] == 0:
                    q.append(i)

        return next(([] for value_ in outbound.values() if value_ != 0), res[::-1])