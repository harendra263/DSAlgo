class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}

        for prerequisite in prerequisites:
            a = prerequisite
            adjList[a[0]].append(a[1])

        outbound = {i:0 for i in range(numCourses)}

        for prerequisite_ in prerequisites:
            a = prerequisite_
            outbound[a[1]] += 1

        q = [i for i in range(numCourses) if outbound[i] == 0]
        while q:
            a = q.pop(0)
            outbound[a] -= 1
            if outbound[a] <= 0:
                q += adjList[a]          

        return all(value <= 0 for value in outbound.values())