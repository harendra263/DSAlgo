class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjList = {(i+1):[] for i in range(n)}
        visited = {(i+1):False for i in range(n)}

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adjList[i+1].append(j+1)

        res = 0
        for i, value in visited.items():
            if value == True: continue
            res += 1
            q = [i]
            while q:
                a = q.pop()
                if visited[a] == True: continue
                visited[a] = True
                q.extend(iter(adjList[a]))
        return res