class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        visited = {i:False for i in range(n)}

        for connect in connections:
            adjList[connect[0]].append(connect[1])
            adjList[connect[1]].append(connect[0])

        q = []
        totalComponent = 0
        for i in adjList:
            if visited[i] == True: continue
            totalComponent += 1
            q.append(i)
            while q:
                comp = q.pop()
                if visited[comp] == True: continue
                visited[comp] = True
                if len(adjList[comp]) > 0:
                    q.extend(i for i in adjList[comp] if visited[i] != True)
        totalCables = len(connections)
        # to connect n computer we need atleast (n-1) cables
        return -1 if totalCables < n-1 else totalComponent - 1
        
                
        